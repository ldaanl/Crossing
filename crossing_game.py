from turtle import Screen
from user import User
from coches import Car
from score import Scoreboard
import time

#* Configuracion de la pantalla de juego
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Crossing")
screen.tracer(0)

#* Inicializando el jugador
user = User((0,-285))

#* Inicializando los coches
car = Car()

#* Inicializando el marcador
score = Scoreboard()

#* Configuracion de movimiento del jugador
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

    #* Si el jugador choca con algun coche
    for i in car.cars:
        if user.distance(i) < 30:
            score.game_over
            band = False
    
    #* Si el jugador atraviesa el tablero
    if user.ycor() >= 250:
        score.points_paddle1
        user.move_home()
        car.reset_cars()


screen.exitonclick()
