from turtle import Turtle

SCORE_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
GAMEOVER = (0, 0)
GAMEOVER_FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.score = 0
        self.highscore = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()



    # def gameover(self):
    #     self.goto(GAMEOVER)
    #     self.write(f"Game Over", False, ALIGNMENT, GAMEOVER_FONT)
