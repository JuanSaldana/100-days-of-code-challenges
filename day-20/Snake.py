from turtle import Turtle
from typing import Union


class SnakeHeadings:
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0


class Snake:
    def __init__(self, color="white"):
        self.head = None
        self.body = []
        self._build_body(color=color)

    @property
    def head_direction(self):
        return self.head.heading()

    @property
    def head_position(self):
        return self.head.pos()

    def _build_body(self, color="white"):
        n = 2
        offset = (20, 0)
        head = Turtle("square")
        self.head = head
        snake_body = [head]
        head.penup()
        self.set_head_direction(self.head_direction)
        self.set_head_position(self.head_position)
        head_pos = head.pos()
        for i in range(n+1)[1::]:
            body_pos = head_pos - (offset[0]*i, offset[1]*i)
            body = Turtle("square")
            body.setpos(body_pos)
            body.penup()
            snake_body.append(body)
        self.body = snake_body
        self.set_color(color)

    def move(self):
        body = self.body.copy()
        body.reverse()
        for element_i in range(len(body[::-2])):
            next_pos = body[element_i+1].pos()
            body[element_i].setpos(next_pos)

        next_pos_add = self.get_next_pos_adder()
        next_pos = self.head_position + next_pos_add

        self.body[0].setpos(next_pos)

        return

    def get_next_pos_adder(self):
        heading = self.head_direction
        if heading == 0:
            next_pos_add = (20, 0)
        elif heading == 90:
            next_pos_add = (0, 20)
        elif heading == 180:
            next_pos_add = (-20, 0)
        elif heading == 270:
            next_pos_add = (0, -20)
        return next_pos_add

    def set_color(self, color: Union[str, tuple]):
        for tim in self.body:
            tim.color(color)

    def set_head_direction(self, direction):
        self.head.setheading(direction)

    def set_head_position(self, x, y=None):
        if isinstance(x, tuple):
            x, y = x
        self.head.setpos((x, y))

    def up(self):
        if self.head_direction == SnakeHeadings.DOWN:
            return
        self.set_head_direction(SnakeHeadings.UP)

    def down(self):
        if self.head_direction == SnakeHeadings.UP:
            return
        self.set_head_direction(SnakeHeadings.DOWN)

    def left(self):
        if self.head_direction == SnakeHeadings.RIGHT:
            return
        self.set_head_direction(SnakeHeadings.LEFT)

    def right(self):
        if self.head_direction == SnakeHeadings.LEFT:
            return
        self.set_head_direction(SnakeHeadings.RIGHT)


if __name__ == "__main__":
    from turtle import Screen
    screen = Screen()
    snake = Snake("black")
    screen.exitonclick()
