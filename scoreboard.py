from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier',15,'italic')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.heading()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

    def scoree(self):
        self.clear()
        self.color("white")
        self.write(f'SCORE : {self.score}', align=ALIGNMENT, font=FONT)
        self.score += 1
    def game_over(self):
        self.home()
        self.write('Game_over!', align=ALIGNMENT, font=FONT)

