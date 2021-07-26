from turtle import Turtle, Screen, back


def reset_screen():
    tim.reset()
    screen.listen()


def clean_screen():
    tim.clear()
    screen.listen()


def forward():
    tim.forward(2)
    screen.listen()


def backward():
    tim.back(2)
    screen.listen()


def clock():
    tim.right(20)


def counter_clock():
    tim.left(20)


if __name__ == "__main__":
    tim = Turtle()
    tim.shape("arrow")
    screen = Screen()
    screen.listen()
    screen.onkeypress(forward, "w")
    screen.onkeypress(backward, "s")
    screen.onkeypress(clock, "d")
    screen.onkeypress(counter_clock, "a")
    screen.onkeypress(clean_screen, "c")
    screen.onkeypress(reset_screen, "r")
    screen.exitonclick()
