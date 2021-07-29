from turtle import Turtle, width
from random import randint


class Food(Turtle):
    def __init__(self, screensize=(600, 600)):
        # food class, its job is to exist and move around when told to
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.screensize = screensize
        self.go_to_random_place()

    def go_to_random_place(self):
        # just move turte to a random place in screen
        offset = 20
        x_max_boundary = (self.screensize[0]/2. - offset)
        x_min_boundary = - x_max_boundary

        y_max_boundary = (self.screensize[1]/2. - offset)
        y_min_boundary = - y_max_boundary

        x = randint(x_min_boundary, x_max_boundary)
        y = randint(y_min_boundary, y_max_boundary)

        self.goto((x, y))


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    screen = Screen()
    screen.setup(width=900, height=900)
    food = Food(screensize=(900, 900))
    while True:
        food.go_to_random_place()
        sleep(1)
