from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)


def set_random_color(turtle: Turtle):
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    turtle.color((r, g, b))


def setup_race(n):
    turtles = []
    screen_size = screen.screensize()
    step = screen_size[1]/n
    initial_pos = step/2.
    y_pos = [initial_pos + i*step + y_offset for i in range(n)]
    x_pos = [20 + x_offset]*n
    for i in range(n):
        turtle = Turtle("turtle")
        turtles.append(turtle)
        turtle.penup()
        set_random_color(turtle)
        turtle.setpos((x_pos[i], y_pos[i]))
    return turtles


def race(turtles):
    winner = None
    while not winner:
        for turtle in turtles:
            turtle.forward(randint(5, 30))
        winner = next(
            (turtle for turtle in turtles if turtle.position()[0] >= race_limit), None)
    return winner


screen = Screen()
x_offset = -500
y_offset = -200
race_limit = 800 + x_offset
size = (400, 1000)
screen.setup(height=size[0], width=size[1])
# screen.setworldcoordinates(-500, -100, 500, 100)
screen.screensize(canvheight=size[0], canvwidth=size[1])
n_turtles = 10
# Setup race
turtles = setup_race(n_turtles)
# ask turtle's name
turtle_id = screen.numinput(
    "Bet for a turtle", f"Pick a number between 0 and {n_turtles-1}")
# Start race
winner = race(turtles)
winner_id = turtles.index(winner)
screen.title(f"WINNER IS TURTLE {winner_id}")
if winner_id == turtle_id:
    message = "YOU WIN"
else:
    message = "YOU LOOSE"
# Print race's output
screen.textinput(message, "Please just enter to leave")
screen.listen()
