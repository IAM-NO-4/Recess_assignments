import tkinter as tk

from game import Game
from agent import Agent
from settings import *


CELL_SIZE = 30
class SnakeDisplay:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Snake - Q Learning")
        self.canvas = tk.Canvas(
            self.root,
            width=GRID_WIDTH * CELL_SIZE,
            height=GRID_HEIGHT * CELL_SIZE,
            bg="white"
        )

        self.canvas.pack()

        self.score_label = tk.Label(
            self.root,
            text="Score: 0"
        )

        self.score_label.pack()
        self.game = Game()
        self.agent = Agent()
        self.agent.qtable.load()
        self.agent.epsilon = 0
        self.run_game()
        self.root.mainloop()


    def draw(self):
        self.canvas.delete("all")
        # Draw snake

        for x, y in self.game.snake.body:
            self.canvas.create_rectangle(
                x * CELL_SIZE,
                y * CELL_SIZE,
                (x + 1) * CELL_SIZE,
                (y + 1) * CELL_SIZE,
                fill="green"
            )

        # Draw food

        fx, fy = self.game.food.position
        self.canvas.create_rectangle(
            fx * CELL_SIZE,
            fy * CELL_SIZE,
            (fx + 1) * CELL_SIZE,
            (fy + 1) * CELL_SIZE,
            fill="red"
        )

        self.score_label.config(
            text=f"Score: {self.game.score}"
        )

    def run_game(self):

        if self.game.game_over:
            self.score_label.config(
                text=f"Game Over! Score: {self.game.score}"
            )

            return
        state = self.agent.get_state(self.game)
        action = self.agent.choose_action(state)
        self.game.step(action)

        self.draw()

        self.root.after(
            200,
            self.run_game
        )
    
if __name__ == "__main__":
    SnakeDisplay()