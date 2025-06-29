import turtle
from turtle import Turtle, Screen
from random import randint

# Instantiate turtle object
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.speed(0)

screen = Screen()
screen.colormode(255)


# # Draw square
# step = 100
# angle = 90
# for i in range(4):
#     timmy_the_turtle.forward(step)
#     timmy_the_turtle.right(angle)

# # Draw dashed line
# for i in range(50):
#     timmy_the_turtle.down()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.up()
#     timmy_the_turtle.forward(10)

# # Draw a bunch of shapes
# for n in range(3, 10):
#     angle = 360 / n
#     timmy_the_turtle.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     for _ in range(n):
#         timmy_the_turtle.forward(75)
#         timmy_the_turtle.right(angle)

# # Draw a random walk
# timmy_the_turtle.pensize(10)
# for n in range(100):
#     angle = randint(0, 3) * 90
#     timmy_the_turtle.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     timmy_the_turtle.right(angle)
#     timmy_the_turtle.forward(25)

# Draw a spirograph
timmy_the_turtle.pensize(2)
num_circles = 50
for n in range(num_circles):
    timmy_the_turtle.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    timmy_the_turtle.right(360 / num_circles)
    timmy_the_turtle.circle(radius=100)

# Persist screen

screen.exitonclick()
