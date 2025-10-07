from turtle import Screen
import time
from modules.snake_module import Snake

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

    screen.exitonclick()

main()