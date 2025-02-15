# Turtle race game

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
game_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
game_on = True

turtle_colors = ["red", "green", "blue", "orange", "yellow", "purple"]
timbu_positions_y_axis = [-70, -40, -10, 20, 50, 80]
all_timbus = []

for i in range(6):
    timbu = Turtle(shape="turtle")
    timbu.color(turtle_colors[i])
    timbu.penup()
    timbu.goto(x=-230, y=timbu_positions_y_axis[i])
    all_timbus.append(timbu)

while game_on:
    for timbu in all_timbus:
        if timbu.xcor() > 230:
            game_on = False
            winning_color = timbu.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


        distance = random.randint(0, 10)
        timbu.forward(distance)

screen.exitonclick()