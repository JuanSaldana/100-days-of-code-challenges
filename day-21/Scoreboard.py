from turtle import Turtle
from time import sleep


class Scoreboard(Turtle):
    def __init__(self, color="white", position=(0, 270)):
        # Create scoreboard
        super().__init__()
        self.position = position
        self.color(color)
        self.speed("fastest")
        self.score = 0
        # we dont' want to see the flaoting object
        self.hideturtle()

        # ideally, it is placed at the top of the screen
        self.goto(self.position)
        self.show()

    def show(self):
        # To show score, erase previous text and update it
        self.clear()
        self.write(f"Score: {self.score}", False,
                   "center", font=("Courier", 15, "bold"))

    def increase_score(self, qty):
        self.update_score(add=qty)
        self.show()

    def reset_score(self):
        # Reset itself
        self.update_score(score=0)
        self.show()

    def update_score(self, add=None, score=None):
        # self explanatory
        if add:
            self.score += add
        elif score:
            self.score = score
        else:
            return

    def game_over(self):
        # if there is game over, go to the center and display GAME OVER
        self.goto(0, 0)
        self.write("GAME OVER", False,
                   "center", font=("Courier", 15, "bold"))


if __name__ == "__main__":
    # main test, should only display a white screen with a scoreboard at the top, and change its value every second
    from turtle import Screen
    screen = Screen()
    screen.setup(width=600, height=600)
    score = Scoreboard("black")
    while True:
        score.show()
        sleep(1)
        score.update_score(1)
