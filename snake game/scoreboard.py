from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("arial",24,"normal")

with open("data.txt") as data_scoreboard: #reads the data file to take the scoreboard
    high_score_data = data_scoreboard.read()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score_data
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", move= False, align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as file_to_write:
                file_to_write.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def add_1(self):
        self.score += 1
        self.update_scoreboard()

