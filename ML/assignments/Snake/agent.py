from qtable import QTable
from settings import *

class Agent:
    def __init__(self):
        self.qtable = QTable()
        self.epsilon = EPSILON

    def get_state(self, game):
        head_x, head_y = game.snake.body[0]
        direction = game.snake.direction
        body = game.snake.body
        food_x, food_y = game.food.position

        # Danger Straight
        if direction == "UP":
            danger_straight = (head_x, head_y - 1) in body or head_y - 1 < 0
            danger_left = (head_x - 1, head_y) in body or head_x - 1 < 0
            danger_right = (head_x + 1, head_y) in body or head_x + 1 >= GRID_WIDTH

        elif direction == "DOWN":
            danger_straight = (head_x, head_y + 1) in body or head_y + 1 >= GRID_HEIGHT
            danger_left = (head_x + 1, head_y) in body or head_x + 1 >= GRID_WIDTH
            danger_right = (head_x - 1, head_y) in body or head_x - 1 < 0

        elif direction == "LEFT":
            danger_straight = (head_x - 1, head_y) in body or head_x - 1 < 0
            danger_left = (head_x, head_y + 1) in body or head_y + 1 >= GRID_HEIGHT
            danger_right = (head_x, head_y - 1) in body or head_y - 1 < 0

        else:  # RIGHT
            danger_straight = (head_x + 1, head_y) in body or head_x + 1 >= GRID_WIDTH
            danger_left = (head_x, head_y - 1) in body or head_y - 1 < 0
            danger_right = (head_x, head_y + 1) in body or head_y + 1 >= GRID_HEIGHT

        return (
            danger_straight,
            danger_left,
            danger_right,

            direction == "UP",
            direction == "DOWN",
            direction == "LEFT",
            direction == "RIGHT",

            food_x < head_x,
            food_x > head_x,
            food_y < head_y,
            food_y > head_y
        )

    def choose_action(self, state):

         return self.qtable.choose_action(
            state,
            self.epsilon
        )
    def learn(
        self,
        state,
        action,
        reward,
        next_state):

        self.qtable.update(
            state,
            action,
            reward,
            next_state,
            LEARNING_RATE,
            DISCOUNT_FACTOR
        )
    
    def decay_epsilon(self):
        if self.epsilon > MIN_EPSILON:
            self.epsilon *= EPSILON_DECAY