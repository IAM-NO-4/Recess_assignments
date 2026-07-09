from game import Game
from agent import Agent
from settings import *

agent = Agent()
best_score = 0
for episode in range(EPISODES):
    game = Game()
    while not game.game_over:
        state = agent.get_state(game)
        action = agent.choose_action(state)
        reward = game.step(action)
        next_state = agent.get_state(game)

        agent.learn(
            state,
            action,
            reward,
            next_state
        )
    if game.score > best_score:
        best_score = game.score
    agent.decay_epsilon()
    if (episode + 1) % 100 == 0:
        print(
            f"Episode: {episode+1} | "
            f"Score: {game.score} | "
            f"Epsilon: {agent.epsilon:.3f}"
        )
print("Training Complete!")
agent.qtable.save()
print("Q-table saved!")