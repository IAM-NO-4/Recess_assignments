# snake.py

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            new_head = (head_x, head_y - 1)

        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)

        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)

        else:
            new_head = (head_x + 1, head_y)

        self.body.insert(0, new_head)
        self.body.pop()
    def grow(self):
        self.body.append(self.body[-1])