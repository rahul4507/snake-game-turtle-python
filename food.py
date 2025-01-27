from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Move food to a random position."""
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)

    def disappear(self):
        """Hide the jackpot turtle."""
        self.hideturtle()

    def create_jackpot(self):
        """Change food appearance for jackpot."""
        self.shape('circle')
        self.color('gold')
        self.shapesize(stretch_len=2, stretch_wid=2)

    def blink_jackpot(self):
        """Make the jackpot food blink."""
        self.color('blue')
        self.shapesize(stretch_len=1, stretch_wid=1)

    def reset_to_normal(self):
        """Reset food to its normal state."""
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_len=1, stretch_wid=1)
