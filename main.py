from turtle import Screen
import time

from modules.scoreboard_module import Scoreboard
from modules.snake_module import Snake
from modules.food_module import Food

screen = Screen()

def restart():
    global screen
    screen.clearscreen()
    main()
    print("restarted")

def main():
    global screen
    screen.setup(width=600, height=600) #keyword arguments
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    game_over = False
    snake = Snake()
    food = Food()

    #Event Listener
    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)
    screen.onkey(key="r", fun=restart)

    #Game running
    while not game_over:
        screen.update()
        time.sleep(0.1)
        snake.move()
        scoreboard = Scoreboard()

        # Detect collision with food.
        if snake.snake_segments[0].distance(food) < 15:
            food.random_position()
            snake.extend()

        # Detect collision with wall.
        if (-280 > snake.snake_segments[0].xcor()
            or snake.snake_segments[0].xcor() > 280
            or -280 > snake.snake_segments[0].ycor()
            or snake.snake_segments[0].ycor() > 280):
            game_over = True

        # Detect collision with tail.
        if len(snake.snake_segments) > 3:
            for segment in snake.snake_segments[1:]:
                if snake.snake_segments[0].distance(segment) < 10:
                    game_over = True

    screen.exitonclick()

main()