"""
Flower drawing program in turtle graphics,
from https://www.youtube.com/watch?v=ekIRrThUfYw

Click on the screen to draw a random flower

"""


import turtle
import random

window = turtle.Screen()
window.setup(1000, 500, 260, 100)

def make_flower_get_position(x, y):
    ""
    make_flower(x, y,
                random.randint(3,10),
                [random.random() for _ in range(3)],
                [random.random() for _ in range(3)] )


def make_flower(x, y, petals, petal_color, center_color):
    ""
    flower = turtle.Turtle()
    flower.hideturtle()
    flower.penup()
    flower.setx(x)
    flower.sety(y)
    flower.color(petal_color)
    for side in range(petals):
        flower.forward(40)
        flower.dot(200 / petals)
        flower.back(40)
        flower.right(360 / petals)

    flower.color(center_color)
    flower.dot(75)

window.onclick(make_flower_get_position)
window.listen()

turtle.done()
