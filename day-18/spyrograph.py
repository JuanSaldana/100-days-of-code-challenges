from turtle import Turtle, Screen, colormode
from random import randint
tim = Turtle()
tim.shape('turtle')
colormode(255)


def set_random_color():
    # generates a random rgb tuple and sets the color
    color_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
    tim.pencolor(color_tuple)


def spyrograph():
    n = 100
    for i in range(n):
        set_random_color()
        tim.circle(100)
        tim.right(360./n)


screen = Screen()
tim.speed('fastest')
spyrograph()
screen.listen()
screen.exitonclick()
