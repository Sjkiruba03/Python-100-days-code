from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high = open("record_score.txt")
        self.data = int(self.high.read())
        self.highscore = self.data
        self.color("white")
        self.up()
        self.goto(0, 230)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score = {self.score} High score = {self.highscore}", align="center", font=("arial", 12, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("arial", 12, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("record_score.txt", mode="w") as data:
                data.write(str(self.highscore))
            # self.high_score()
        self.score = 0
        self.update_score()

    def calculate_score(self):
        self.score += 1
        # self.clear()
        self.update_score()

