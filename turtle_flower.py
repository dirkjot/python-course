"""
Flower drawing program in turtle graphics,
from https://www.youtube.com/watch?v=ekIRrThUfYw

Click on the screen to draw a random flower

"""


import turtle
import random
import sys


window = turtle.Screen()
window.setup(1000, 500, 260, 100)

def make_flower_get_position(x, y):
    """
    Routine that listens to window events, it will be
    called with the x,y of the mouse click
    """
    make_flower(x, y,
                random.randint(3,10),
                [random.random() for _ in range(3)],
                [random.random() for _ in range(3)] )


def make_flower(x, y, petals, petal_color, center_color):
    """
    Draw a flower at position x,y, with 'petals' number of
    petals and using colors
    """
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
    print("make_flower(x={}, y={}, petals={}, petal_color={}, center_color={})".format(
        x, y, petals, petal_color, center_color
    ))


def main():
    """
    First ran 'main_old' (below) a few times and clicked randomly.
    This looked nice and I captured it from the print messages
    I rounded the color numbers so it is easier to read.
    """
    make_flower(x=112.0, y=49.0, petals=9, petal_color=[0.691, 0.952, 0.933], center_color=[0.474, 0.135, 0.776])
    make_flower(x=-68.0, y=-95.0, petals=7, petal_color=[0.181, 0.563, 0.706], center_color=[0.614, 0.701, 0.063])
    make_flower(x=29.0, y=-26.0, petals=5, petal_color=[0.471, 0.115, 0.637], center_color=[0.639, 0.072, 0.988])
    make_flower(x=-64.0, y=34.0, petals=6, petal_color=[0.173, 0.823, 0.970], center_color=[0.290, 0.376, 0.607])
    # need to call this or the screen will go away immediately
    turtle.done()


def main_old():
    ""
    window.onclick(make_flower_get_position)
    window.listen()
    turtle.done()


if __name__ == "__main__":
    print(sys.version_info)
    main()

