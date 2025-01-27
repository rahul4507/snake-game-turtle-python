from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'italic')
GAME_OVER_FONT = ('Arial', 20, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.score += 1
        self.update_scoreboard()

    def increase_score(self):
        self.score += 5
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
