import random
import pickle
class QTable:
    def __init__(self):
        self.table = {}
    
    def get_values(self, state):
        if state not in self.table:
            self.table[state] = [0.0, 0.0, 0.0]
        return self.table[state]
    
    def choose_action(self, state, epsilon):
        values = self.get_values(state)
        if random.random() < epsilon:
            return random.randint(0, 2)
        return values.index(max(values))
    

    def update(self, state, action, reward, next_state,
           learning_rate, discount_factor):
        current = self.get_values(state)[action]
        future = max(self.get_values(next_state))
        new_value = current + learning_rate * (
            reward + discount_factor * future - current
        )
        self.table[state][action] = new_value

    def save(self, filename="qtable.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.table, file)

    def load(self, filename="qtable.pkl"):
        try:
            with open(filename, "rb") as file:
                self.table = pickle.load(file)
        except FileNotFoundError:
            print("No saved Q-table found. Starting fresh.")