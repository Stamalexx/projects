from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("arial",24,"normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"{self.l_score}     {self.r_score}",move= False,align=ALIGNMENT,font=FONT)
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"{self.l_score}     {self.r_score}",move= False,align=ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", move= False, align=ALIGNMENT, font=FONT)

    def add_1_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
    def add_1_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()