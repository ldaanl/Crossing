from turtle import Turtle
from random import choice,randint

COLORS = ["white", "yellow", "blue", "purple", "red", "green"]

class Car():

    def __init__(self):
        self.cars = []
        self.init_car()
    
    def init_car(self):
        r = randint(1,6)
        if r == 1:
            car = Turtle("square")
            car.color(choice(COLORS))
            car.pu()
            car.turtlesize(1,3)
            car.goto(300,randint(-250,250))
            self.cars.append(car)
    
    def move_cars(self):
        for i in self.cars:
            i.backward(10)
    
    def reset_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        self.init_car()

