from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()


# Etch-a-sketch app
def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def rotate_clockwise():
    turtle.right(10)


def rotate_counter_clockwise():
    turtle.left(10)


def clear_screen():
    turtle.clear()
    turtle.up()
    turtle.home()
    turtle.down()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=rotate_clockwise, key="d")
screen.onkey(fun=rotate_counter_clockwise, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
