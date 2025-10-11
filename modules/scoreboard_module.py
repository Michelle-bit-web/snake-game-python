from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
FONT_GAMEOVER = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.up()
        self.score_p1 = 0
        self.score_p2 = 0
        with open("highscore_data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        if self.player == 2:
            self.write(f"Player 1: {self.score_p1} Player 2: {self.score_p2}", False, align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Score: {self.score_p1} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self, player_color):
        if player_color == "white":
            self.score_p1 += 1
        else:
            self.score_p2 += 1
        self.update_scoreboard()

    def check_new_highscore(self):
        return self.score_p1 > self.highscore

    def show_endscreen(self):
        if self.check_new_highscore() and self.player == 1:
            self.highscore = self.score_p1
            with open("highscore_data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
            self.score_p1 = 0
            self.score_p2 = 0
        self.update_scoreboard()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT,font=FONT)
        self.goto(0, -60)
        self.write(f"Press 'r' to replay\nClick window to exit", False, align=ALIGNMENT, font=FONT_GAMEOVER)
