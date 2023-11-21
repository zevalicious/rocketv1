import turtle
import random
#pc starts @ 0 black = 0
turtlecolors = ['black','pink','teal','violet','green','red',
                'orange','blue']
jemma = turtle.Turtle()
sophie = turtle.Turtle()
terry = turtle.Turtle()
cturt = sophie
def square():
    x = random.randint(-180,180)
    cturt.color(random.choice(turtlecolors))
    cturt.penup()
    cturt.left(x)
    cturt.forward(x)
    cturt.pendown()
    for i in range(4):
        cturt.forward(x)
        cturt.right(90)
square()
cturt = jemma
square()
cturt = terry
square()
