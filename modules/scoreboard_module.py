from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
FONT_GAMEOVER = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.score = 0
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

