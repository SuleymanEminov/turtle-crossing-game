import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# State machine to track which keys are pressed
keys_pressed = {}

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


def main():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        scoreboard.update_score()
        car_manager.create_car()
        car_manager.move()

        # Check state of key presses and respond accordingly
        if keys_pressed["Up"] or keys_pressed["w"]: player.move()

        # Detect collision with cars
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # Check if the player reached the finish line
        if player.ycor() == 290:
            player.reset_position()
            scoreboard.gain_score()
            scoreboard.update_score()


# Callback for KeyPress event listener. Sets key pressed state to True
def pressed(event):
    keys_pressed[event.keysym] = True


# Callback for KeyRelease event listener. Sets key pressed state to False
def released(event):
    keys_pressed[event.keysym] = False


# Setup the event listeners, bypassing the Turtle Screen to use the underlying TKinter canvas directly
# This needs to be done to get access to the event object so the state machine can determine which key was pressed
def set_key_binds():
    for key in ["Up","w"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False




screen.listen()
set_key_binds()
main()

screen.exitonclick()


