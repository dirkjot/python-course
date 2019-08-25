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
    ""
    window.onclick(make_flower_get_position)
    window.listen()
    turtle.done()


if __name__ == "__main__":
    print(sys.version_info)
    main()

