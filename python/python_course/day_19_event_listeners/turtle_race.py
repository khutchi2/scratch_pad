from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=600, height=500)
screen.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def make_turtles():
    red = Turtle()
    orange = Turtle()
    yellow = Turtle()
    green = Turtle()
    blue = Turtle()
    purple = Turtle()
    return [red, orange, yellow, green, blue, purple]


# Make Turtles
turtle_list = make_turtles()
y_vals = [30 * i for i in range(7)]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for turt, color, y in zip(turtle_list, colors, y_vals):
    turt.shape("turtle")
    turt.up()
    turt.color(color)
    turt.sety(y)
    turt.setx(-250)
    turt.speed(0)

# Input
prediction = screen.textinput("Place Your Bets!", "Which turtle do you think will win?")

# Race Turtles
while 250 not in [turt.xcor() for turt in turtle_list]:
    print([turt.xcor() for turt in turtle_list])
    for turt in turtle_list:
        turt.forward(randint(1, 10))

# Determine winner
winner = [turt.xcor() for turt in turtle_list]
winner_idx = winner.index(True)
winner = colors[winner_idx]


if prediction == winner:
    print("Your turtle won!")
else:
    print("Your turtle did not win, better luck next time!")


# screen.exitonclick()
