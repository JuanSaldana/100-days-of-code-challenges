from random import choice
from time import sleep
from turtle import Turtle, heading, position
from typing import Union


class SnakeHeadings:
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0


class Snake:
    # Snake class
    def __init__(self, color="white", length=3):
        self.head = None
        self.body = []
        self.color = color
        self._build_body(color=color, length=length)

    @property
    def snake_body(self):
        # Since we have a mutating property, invoque property decorator
        if len(self.body) > 1:
            return self.body[1::]
        else:
            return self.body

    @property
    def head_direction(self):
        # here too
        return self.head.heading()

    @property
    def head_position(self):
        # and here
        return self.head.pos()

    def _build_body(self, color="white", length=3):
        # Instate the head, then grow the number of times specified
        n = length
        head = Turtle("square")
        self.head = head
        head.penup()
        self.body = [head]
        self.set_head_direction(self.head_direction)
        self.set_head_position(self.head_position)
        for i in range(n+1)[1::]:
            self.grow()
        self.set_color(color)

    def move(self):
        # To move the whole snake, we move each piece to replace previous piece's place
        # Like a worm
        body = self.body.copy()
        # So we start from the back
        body.reverse()
        for element_i in range(len(body[:-1])):
            # go to the previous piece's position
            next_pos = body[element_i+1].pos()
            next_heading = body[element_i+1].heading()
            body[element_i].setpos(next_pos)
            # and get its heading too, this is only for growing purposes
            body[element_i].setheading(next_heading)

        # finally, move the head by considering its direction
        next_pos_add = self.get_next_pos_adder(self.head_direction)
        next_pos = self.head_position + next_pos_add

        self.head.setpos(next_pos)

        return

    def get_next_pos_adder(self, heading):
        # get next position adder to get to tell the head where to go to, could also use forward?
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
        # set all snake's color
        for tim in self.body:
            tim.color(color)

    def set_head_direction(self, direction):
        # wrapper method for turtle.setheading
        self.head.setheading(direction)

    def set_head_position(self, x, y=None):
        # wrapper method for turtle.setpos
        if isinstance(x, tuple):
            x, y = x
        self.head.setpos((x, y))

    def up(self):
        # wrapper method to tell snake where to look
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

    def is_intersecting(self):
        # check if snake is intersecting itself
        snake_body = self.snake_body
        if len(snake_body) > 3:
            if any(self.head.distance(bod) < 10 for bod in snake_body):
                return True
        return False

    def grow(self):
        # Adds a new piece to the back of the snake.

        # To know where to put it, just get the last piece's heading and position
        heading = self.snake_body[-1].heading()
        # Then the new piece's place shall be at the opposite direction
        position = self.snake_body[-1].pos() - self.get_next_pos_adder(heading)

        # create it
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color(self.color)
        new_seg.setposition(position)
        new_seg.setheading(heading)

        # incorporate it to the snake's body
        self.body.append(new_seg)


if __name__ == "__main__":
    # main test
    # Just creates a snake and moves it a little bit
    from turtle import Screen
    screen = Screen()
    screen.tracer(0)
    snake = Snake("black")
    random_moves = [snake.up, snake.down, snake.left, snake.right]
    while True:
        snake.move()
        method = choice(random_moves)
        method()
        screen.update()
        sleep(0.1)
