from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
from turtle import Screen, Turtle, screensize, width
from time import sleep


class SnakeGame:
    def __init__(self, screensize=(600, 600), snake_length=3):
        # creates all necessary objects to start game

        # initialize screen
        self.screen = Screen()
        self.screen.setup(height=screensize[1], width=screensize[0])
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        # create snake
        self.snake = Snake(color="white", length=snake_length)

        # Associates and creates food
        self.food = Food()

        # Scoreboard, to be at the top of the screen
        self.score_board = Scoreboard(
            color="white", position=(0, screensize[1]/2. - 30))

        # All other setups, like game functions
        self.setup()

    def setup(self):
        self.screen.onkey(self.snake.up, "w")
        self.screen.onkey(self.snake.down, "s")
        self.screen.onkey(self.snake.left, "a")
        self.screen.onkey(self.snake.right, "d")
        return

    # returns the game's score through scoreboard
    @property
    def score(self):
        return self.score_board.score

    # basic functionality to see if there was a colission between snake and forbidden places
    @property
    def has_collisioned(self):
        screensize = self.screen.window_width(), self.screen.window_height()
        offset = 15
        x_max_bound = (screensize[0]/2. - offset)
        x_min_bound = - x_max_bound
        y_max_bound = (screensize[1]/2. - offset)
        y_min_bound = - y_max_bound
        # if snake has trespassed the boundaries of the screen
        if not (x_min_bound < self.snake.head.xcor() < x_max_bound) or \
           not (y_min_bound < self.snake.head.ycor() < y_max_bound):
            return True
        # or if the snake is touching itself with its head
        elif self.snake.is_intersecting():
            return True
        # if not, then we good
        else:
            return False

    # If the snake has reached its food, then it has scored
    @property
    def has_scored(self):
        if self.snake.head.distance(self.food) < 20:
            return True
        else:
            return False

    # We increase score by invoking this methods
    def increase_score(self):
        self.score_board.increase_score(1)
        self.food.go_to_random_place()

    # main game run like this:
    def main_game(self):
        game_on = True
        # while we haven't lost
        while game_on:
            # play the game
            self.play()
            # if there was a colission, then game must be stopped
            if self.has_collisioned:
                game_on = False
            # if there was a scoring
            if self.has_scored:
                self.increase_score()
                self.snake.grow()

        # if we go out of the main loop, then it's game over
        self.game_over()

    def play(self, interval=0.04):
        # play if just to move snake around and refresh screen
        self.screen.listen()
        self.snake.move()
        self.screen.update()
        self.score_board.show()
        sleep(interval)

    # other interesting methods
    def clear(self):
        return

    def restart(self):
        self.clear()
        self.start()

    def game_over(self):
        self.score_board.game_over()
        self.screen.exitonclick()
        exit()


if __name__ == "__main__":
    # main test
    snake_game = SnakeGame(screensize=(900, 900))
    snake_game.main_game()
