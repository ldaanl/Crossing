from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score1 = 1
        self.scoreboard
    
    @property
    def scoreboard(self):
        self.goto(-250,250)
        self.write(f'Nivel : {self.score1}', align='center', font = ('Arial', 15, 'normal'))
    
    @property
    def points_paddle1(self):
        self.score1 += 1
        self.clear()
        self.scoreboard
    
    @property
    def game_over(self):
        self.home()
        self.color("red")
        self.write('GAME OVER', align='center', font = ('Arial', 30, 'normal'))
