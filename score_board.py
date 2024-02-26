from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_highscore()
        self.score = 0
        self.write_score()

    @staticmethod
    def read_highscore():
        with open("data.txt") as file:
            contents = file.read()
            return int(contents)

    def store_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
