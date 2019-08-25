"""
Flower drawing program in turtle graphics,
from https://www.youtube.com/watch?v=ekIRrThUfYw

Click on the screen to draw a random flower

"""


import turtle
import random
import sys



yellow = [1, 1, 0]


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
    flower.speed(0)
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


def warhol(origin_x=0, origin_y=0, background_color=yellow):
    """
    - Refactored to only use four colors, should choose some prettier ones
    - The background color is not used yet
    """
    color1 = [0.691, 0.952, 0.933]
    color2 = [0.181, 0.563, 0.706]
    color3 = [0.471, 0.115, 0.637]
    color4 = [0.290, 0.376, 0.607]


    make_flower(x=origin_x + 112.0, y=origin_y + 49.0, petals=9, petal_color=color1, center_color=color3)
    make_flower(x=origin_x + -68.0, y=origin_y + -95.0, petals=7, petal_color=color2, center_color=color1)
    make_flower(x=origin_x + 29.0, y=origin_y + -26.0, petals=5, petal_color=color3, center_color=color1)
    make_flower(x=origin_x + -64.0, y=origin_y + 34.0, petals=6, petal_color=color2, center_color=color4)




def main():
    "New main routine that does screen setup and calls a warhol"
    window = turtle.Screen()
    window.setup(1000, 500, 260, 100)
    warhol(0,0)
    # need to call this or the screen will go away immediately
    turtle.done()


if __name__ == "__main__":
    print(sys.version_info)
    main()

