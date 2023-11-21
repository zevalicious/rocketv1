import turtle
import random
bailey=turtle.Turtle()
bailey.shape('turtle')
bailey.speed(999999)
turtlecolors = ['black','pink','teal','violet','green','red',
                'orange','blue']
def randomillusion():
    bailey.penup
    x = random.randint(-180,180)
    bailey.color(random.choice(turtlecolors))
    bailey.left(x)
    bailey.forward(x)
    bailey.pendown
    for i in range(x*2):
        bailey.forward(x)
        bailey.right(x)
    bailey.penup
    bailey.goto(0,0)
    bailey.pendown

randomillusion()
randomillusion()
randomillusion()
randomillusion()
randomillusion()
