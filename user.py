from turtle import Turtle

class User(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.pu()
        self.left(90)
        self.goto(pos)
    
    def move_up(self):
        y = self.ycor() + 10
        self.goto(self.xcor(), y)
    
    def move_down(self):
        y = self.ycor() - 10
        self.goto(self.xcor(), y)
    
    def move_right(self):
        x = self.xcor() + 10
        self.goto(x, self.ycor())
    
    def move_left(self):
        x = self.xcor() - 10
        self.goto(x, self.ycor())
    
    def move_home(self):
        self.goto(0,-285)