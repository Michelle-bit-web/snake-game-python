from turtle import Screen
from modules.snake_module import Snake
from modules.food_module import Food
from modules.scoreboard_module import Scoreboard
import time

class Game:
    def __init__(self, players):
        self.screen = Screen()
        self.food = Food()
        self.players = players
        self.scoreboard = Scoreboard(players)
        self.snakes = [Snake('white')]
        if players == 2:
            self.snakes.append(Snake('green'))
        self.game_over = False

        self.setup_screen()
        self.bind_controls()
        self.screen.onkey(self.restart, "r")

    def setup_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)

    def bind_controls(self):
        self.screen.listen()
        # Player 1 controls
        self.screen.onkey(self.snakes[0].move_up, "Up")
        self.screen.onkey(self.snakes[0].move_down, "Down")
        self.screen.onkey(self.snakes[0].move_left, "Left")
        self.screen.onkey(self.snakes[0].move_right, "Right")

        # Player 2 controls (only if second snake exists)
        if self.players == 2:
            snake_two = self.snakes[1]
            self.screen.onkey(snake_two.move_up, "w")
            self.screen.onkey(snake_two.move_down, "s")
            self.screen.onkey(snake_two.move_left, "a")
            self.screen.onkey(snake_two.move_right, "d")

    def game_loop(self):
        while not self.game_over:
            self.screen.update()
            time.sleep(0.1)
            for snake in self.snakes:
                snake.move()
            self.check_collisions()

        self.screen.exitonclick()

    def check_collisions(self):
        for snake in self.snakes:
            if self.hit_wall(snake) or self.hit_self(snake):
                self.end_game()
                return
            if self.hit_food(snake):
                self.food.random_position()
                snake.extend()
                self.scoreboard.increase_score(snake.color)
        if len(self.snakes) == 2:
            self.check_snake_vs_snake(self.snakes[0], self.snakes[1])

    def hit_wall(self, snake):
        head = snake.snake_segments[0]
        return not (-280 < head.xcor() < 280 and -280 < head.ycor() < 280)

    def hit_self(self, snake):
         for segment in snake.snake_segments[1:]:
            if snake.snake_segments[0].distance(segment) < 10:
                return True
            return False

    def hit_food(self, snake):
        return snake.snake_segments[0].distance(self.food) < 15

    def check_snake_vs_snake(self, snake_1, snake_2):

        for segment in snake_2.snake_segments[1:]:
            if snake_1.snake_segments[0].distance(segment) < 10:
                self.end_game()
                return
        for segment in snake_1.snake_segments[1:]:
            if snake_2.snake_segments[0].distance(segment) < 10:
                self.end_game()
                return

    def end_game(self):
        self.scoreboard.show_endscreen()
        self.game_over = True

    def restart(self):
        self.screen.clearscreen()
        new_game = Game(self.players)
        new_game.game_loop()