import turtle
from turtle import Turtle, Screen
import colorgram
from random import choice
from PIL import Image

turtle = Turtle()
turtle.shape("turtle")
turtle.color("green")
turtle.speed(0)
screen = Screen()
screen.colormode(255)

# Extract color pallette
picture = "damien_hirst_spots.jpg"
extracted_colors = colorgram.extract(picture, 50)
turtle.up()
x_0 = -300
y_0 = -300
turtle.goto(x_0, y_0)
for y in range(20):
    turtle.up()
    turtle.goto(x_0, y_0 + y * 40)
    for _ in range(20):
        color = choice(extracted_colors)
        turtle.down()
        turtle.pencolor(color.rgb)
        turtle.dot(size=15)
        turtle.up()
        turtle.forward(40)

turtle.hideturtle()

# Save image as eps
file_name = "dots.eps"
ts = turtle.getscreen()
ts.getcanvas().postscript(file=file_name)

# Convert to png
im = Image.open(file_name)
fig = im.convert("RGBA")
image_png = "dots.png"
fig.save(image_png, lossless=True)

screen.exitonclick()
