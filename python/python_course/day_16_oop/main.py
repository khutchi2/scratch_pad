from turtle import Turtle, Screen

# Turtle is a Python standard library graphics library
timmy: Turtle = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkViolet")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()