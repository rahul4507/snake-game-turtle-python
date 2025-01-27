from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


class GameController:
    def __init__(self):
        # Initialize the screen
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.setup(width=800, height=800)
        self.screen.bgcolor('black')
        self.screen.tracer(0)

        # Initialize game components
        self.snake = None
        self.food = None
        self.scoreboard = None
        self.is_game_on = False
        self.jackpot_active = False
        self.jackpot_food = None  # Jackpot food (separate from normal food)

        # Create start message
        self.start_message = Turtle()
        self.start_message.hideturtle()
        self.start_message.color('white')
        self.start_message.penup()
        self.start_message.goto(0, 0)
        self.start_message.write("Press SPACE to start", align="center", font=("Arial", 24, "normal"))

        # Border turtle
        self.border = None

        # Set up key bindings
        self.screen.listen()
        self.screen.onkey(self.start_game, 'space')
        self.screen.onkey(self.exit_game, 'Escape')

    def draw_border(self):
        """Draw the game border."""
        self.border = Turtle()
        self.border.hideturtle()
        self.border.speed('fastest')
        self.border.color('white')
        self.border.penup()
        self.border.goto(-390, 390)
        self.border.pendown()
        for _ in range(4):
            self.border.forward(780)
            self.border.right(90)

    def clear_game(self):
        """Clear all game components."""
        if self.snake:
            for segment in self.snake.all_segments:
                segment.hideturtle()
            self.snake = None

        if self.food:
            self.food.hideturtle()
            self.food = None

        if self.scoreboard:
            self.scoreboard.clear()
            self.scoreboard = None

        if self.jackpot_food:
            self.jackpot_food.hideturtle()
            self.jackpot_food = None

        if self.border:
            self.border.clear()
            self.border = None

        self.screen.update()

    def start_game(self):
        """Initialize and start the game."""
        if not self.is_game_on:
            self.start_message.clear()
            self.clear_game()
            self.draw_border()

            self.snake = Snake()
            self.food = Food()  # Normal food
            self.scoreboard = ScoreBoard()

            self.screen.listen()
            self.screen.onkey(self.snake.up, 'Up')
            self.screen.onkey(self.snake.down, 'Down')
            self.screen.onkey(self.snake.right, 'Right')
            self.screen.onkey(self.snake.left, 'Left')

            self.is_game_on = True
            self.jackpot_active = False
            self.jackpot_food = None  # Ensure jackpot food is None at start
            self.game_loop()

    def game_loop(self):
        """Main game loop."""
        while self.is_game_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            # Detect collision with normal food
            if self.jackpot_active:
                if self.snake.head.distance(self.jackpot_food) < 15:
                    self.scoreboard.increase_score()  # Jackpot points
                    self.snake.extend()
                    self.snake.extend()
                    self.snake.extend()
                    self.snake.extend()
                    self.snake.extend()
                    self.jackpot_active = False
                    self.jackpot_food.hideturtle()
                    self.jackpot_food = None  # Remove jackpot food after collection

            if self.snake.head.distance(self.food) < 15:
                self.scoreboard.track_score()  # Normal food points
                self.food.refresh()
                self.snake.extend()

                # Trigger jackpot every 6 points
                if self.scoreboard.score % 6 == 0 and not self.jackpot_active:
                    self.trigger_jackpot()

            # Detect collision with wall
            if (
                self.snake.head.xcor() > 390
                or self.snake.head.xcor() < -390
                or self.snake.head.ycor() > 390
                or self.snake.head.ycor() < -390
            ):
                self.is_game_on = False

            # Detect collision with tail
            for segment in self.snake.all_segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.is_game_on = False

        self.scoreboard.reset_score()
        self.game_over()

    def trigger_jackpot(self):
        """Activate the jackpot."""
        self.jackpot_active = True
        self.jackpot_food = Food()  # Create a separate jackpot food
        self.jackpot_food.create_jackpot()

        # Blink and deactivate jackpot after 1 second if not taken
        self.screen.ontimer(self.deactivate_jackpot, 10000)

    def deactivate_jackpot(self):
        """Deactivate the jackpot if not collected."""
        if self.jackpot_active:
            self.jackpot_food.blink_jackpot()
            self.jackpot_food.hideturtle()
            self.jackpot_food = None
            self.jackpot_active = False

    def game_over(self):
        """Handle game over state."""
        self.start_message.clear()
        self.start_message.write("Game Over! Press SPACE to play again\nPress ESC to exit",
                                 align="center", font=("Arial", 24, "normal"))
        self.clear_game()
        self.screen.update()

    def exit_game(self):
        """Exit the game."""
        self.screen.bye()


def main():
    game = GameController()
    game.screen.mainloop()

if __name__ == '__main__':
    main()