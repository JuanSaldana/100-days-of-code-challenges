from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')

colors = ["red", "red", "yellow", "grey", "pink",
          "black", "green", "blue", "brown", "red"]


def polygon(n: int):
    """Generate a n-side polygon on screen

    Args:
        n (int): The number of sides of the polygon
    """
    # because of the extension of the colors list, this function only supports up to 10 sides
    tim.color(colors[n])
    for i in range(n):
        tim.forward(100)
        tim.right(360./n)


# defining all simple routines to draw each individual figure
def line(): return polygon(2)
def triangle(): return polygon(3)
def square(): return polygon(4)
def pentagon(): return polygon(5)
def hexagon(): return polygon(6)
def heptagon(): return polygon(7)
def octagon(): return polygon(8)
def nonegon(): return polygon(9)
def decagon(): return polygon(10)


# routine to execute all other routines
def all_polygons():
    line()
    triangle()
    square()
    pentagon()
    hexagon()
    heptagon()
    octagon()
    nonegon()
    decagon()


# script to show things on screen
screen = Screen()
screen.onkeypress(line, "2")
screen.onkeypress(triangle, "3")
screen.onkeypress(square, "4")
screen.onkeypress(pentagon, "5")
screen.onkeypress(hexagon, "6")
screen.onkeypress(heptagon, "7")
screen.onkeypress(octagon, "8")
screen.onkeypress(nonegon, "9")
screen.onkeypress(decagon, "0")
screen.onkeypress(all_polygons, "a")
screen.listen()
screen.exitonclick()
