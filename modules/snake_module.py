from turtle import Turtle

STARTING_POSITION = [(0,0)]
MOVE_STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self, color):
        self.color = color
        self.snake_segments = []
        self.create_snake(self.color)

    def create_snake(self, color):
        for coordinate in STARTING_POSITION:
            self.add_segment(coordinate, color)

    def add_segment(self, position, color):
        segment = Turtle()
        segment.shape("square")
        segment.color(color)
        segment.up()
        segment.goto(position)
        self.snake_segments.append(segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position(), self.color)

    def move(self):
        for seg_number in range(len(self.snake_segments) - 1, 0, -1):  # start, stop, step
            new_x = self.snake_segments[seg_number - 1].xcor()
            new_y = self.snake_segments[seg_number - 1].ycor()
            self.snake_segments[seg_number].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_STEPS)

    def move_up(self):
        if self.snake_segments[0].heading() == DOWN:
            return
        self.snake_segments[0].setheading(UP)

    def move_down(self):
        if self.snake_segments[0].heading() == UP:
            return
        self.snake_segments[0].setheading(DOWN)

    def move_left(self):
        if self.snake_segments[0].heading() == RIGHT:
            return
        self.snake_segments[0].setheading(LEFT)

    def move_right(self):
        if self.snake_segments[0].heading() == LEFT:
            return
        self.snake_segments[0].setheading(RIGHT)