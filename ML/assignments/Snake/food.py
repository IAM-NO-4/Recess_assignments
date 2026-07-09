import random

class Food:

    def __init__(self):
        self.position = (0, 0)

    def spawn(self, snake_body, width, height):

        while True:

            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)

            if (x, y) not in snake_body:
                self.position = (x, y)
                break