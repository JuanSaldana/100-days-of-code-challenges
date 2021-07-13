from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color("red")

def moving():
    tim.forward(100)
    
screen = Screen()
screen.onkey(moving, "a")
screen.listen()
screen.exitonclick()