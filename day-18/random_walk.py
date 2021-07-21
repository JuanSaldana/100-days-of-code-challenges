from turtle import Turtle, Screen, colormode
from random import randint, choice

tim = Turtle()
tim.shape('turtle')
tim.pensize(15.2)
colormode(255)


def set_random_color():
    # generates a random rgb tuple and sets the color
    color_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
    tim.pencolor(color_tuple)


def random_square_walk():
    # just takes a random step, infinitely
    step = 0
    while True:
        step += 1
        random_step()


def random_step():
    # changes width to get it thicker each time
    width = tim.width()
    width += (width)/100
    tim.pensize(width)
    # length
    length = randint(15, 70)
    turn = choice([0, 90, 180, 270])
    set_random_color()
    tim.setheading(turn)
    tim.forward(length)


# script to show on screen the stuff
screen = Screen()
screen.onkeypress(random_square_walk, "r")
screen.listen()
screen.exitonclick()
