from hashlib import new
from os import supports_follow_symlinks
from color_extraction import COLORS
from turtle import Turtle, Screen, colormode
from random import randint, choice
tim = Turtle()
tim.shape('arrow')
tim.hideturtle()
colormode(255)


def get_random_color():
    return choice(COLORS)


def set_random_color():
    pen_color = get_random_color()
    tim.pencolor(pen_color)


def split_canvas(grid: tuple, split: tuple):
    # splits a 2D grid homogeneously and returns all centers positions
    positions = []
    x_step = grid[0] / split[0]
    y_step = grid[1] / split[1]
    x_initial_pos = x_step/2.
    y_initial_pos = y_step/2.
    initial_pos = (x_initial_pos, y_initial_pos)
    # for j in range(split[1]):
    #     y_pos = y_initial_pos + j * y_step
    #     for i in range(split[0]):
    #         x_pos = x_initial_pos + i * x_step
    #         new_pos = (x_pos, y_pos)
    #         positions.append(new_pos)
    positions = [(x_initial_pos + i * x_step, y_initial_pos + j * y_step)
                 for i in range(split[0]) for j in range(split[1])]
    return positions


def HirstPainting():
    tim.hideturtle()
    positions = split_canvas(canvas_size, split_size)
    tim.penup()
    for pos in positions:
        tim.setpos(pos)
        set_random_color()
        tim.pendown()
        tim.dot(size=min(canvas_size[0]/split_size[0],
                canvas_size[1]/split_size[1])/2.)
        tim.penup()


screen = Screen()
canvas_size = (1000, 1000)
split_size = (100, 100)
screen.screensize(canvheight=canvas_size[0], canvwidth=canvas_size[1])
screen.setworldcoordinates(-100, -100, 1000, 1000)
tim.speed('fastest')
HirstPainting()
screen.listen()
screen.exitonclick()
