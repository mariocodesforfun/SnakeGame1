from asyncore import read
from importlib.resources import contents
from statistics import mode
from tkinter import W
from turtle import Turtle
from asyncore import read


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.speed("fastest")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = (data.read())
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
                self.score = 0
                self.update_scoreboard()

            





    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
            



