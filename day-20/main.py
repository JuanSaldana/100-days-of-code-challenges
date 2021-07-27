from turtle import Turtle, Screen
from Snake import Snake
from time import sleep


def main_game():
    while True:
        screen.listen()
        snake.move()
        screen.update()
        sleep(0.04)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
snake = Snake()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.tracer(0)
main_game()
