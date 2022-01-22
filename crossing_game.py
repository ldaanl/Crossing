from turtle import Screen
from user import User
from coches import Car
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Crossing")
screen.tracer(0)

user = User((0,-285))
car = Car()

screen.listen()
screen.onkey(user.move_up, "w")
screen.onkey(user.move_down, "s")
screen.onkey(user.move_right, "d")
screen.onkey(user.move_left, "a")

band, cont = True, 0
while band:
    time.sleep(0.1)
    screen.update()
    car.init_car()
    car.move_cars()
    for i in car.cars:
        if user.distance(i) < 40:
            band = False



screen.exitonclick()
