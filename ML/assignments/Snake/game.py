from snake import Snake
from food import Food
from settings import *
class Game:

    def __init__(self):

        self.snake = Snake()

        self.food = Food()

        self.food.spawn(
            self.snake.body,
            GRID_WIDTH,
            GRID_HEIGHT
        )

        self.score = 0

        self.game_over = False
    def check_collision(self):
        head = self.snake.body[0]
        x, y = head
        if x < 0 or x >= GRID_WIDTH:
            return True
        if y < 0 or y >= GRID_HEIGHT:
            return True
        if head in self.snake.body[1:]:
            return True
        return False
    def check_food(self):
        if self.snake.body[0] == self.food.position:
            self.score += 1
            self.snake.grow()
            self.food.spawn(
                self.snake.body,
                GRID_WIDTH,
                GRID_HEIGHT
            )
            return True
        return False
    
    def step(self, action):
        self.apply_action(action)
        self.snake.move()
        if self.check_collision():
            self.game_over = True
            return -100
        if self.check_food():
            return 10
        return -1
    
    def apply_action(self, action):
        directions = ["UP", "RIGHT", "DOWN", "LEFT"]
        index = directions.index(self.snake.direction)
        if action == 1:
            index = (index - 1) % 4
        elif action == 2:
            index = (index + 1) % 4
        self.snake.direction = directions[index]
    