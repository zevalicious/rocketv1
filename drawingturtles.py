import turtle
import random
tyrone = turtle.Turtle()
tyrone.shape("turtle")
tyrone.speed(9000)


tyler = turtle.Turtle()
tyler.shape("turtle")
tyler.speed(9000)

def left():
    tyrone.left(90)
def right():
    tyrone.right(90)
def go():
    tyrone.forward(50)
def back():
    tyrone.left(180)
def up():
    tyrone.penup()
def down():
    tyrone.pendown()
for i in range (4):
    go()
    right()
right()
for i in range (8):
    go()
    tyrone.right(45)
tyrone.penup()
tyrone.forward(143)
tyrone.pendown()
x = random.randint(5,50)
tyler.forward(80)
for i in range(4):
    tyler.color('blue')
    tyler.forward(25)
    tyler.right(90)
tyrone.penup()
tyrone.forward(100)
tyrone.pendown()
tyrone.begin_fill()
tyrone.color('orange')
for i in range (5):
    go()
    tyrone.right(72)
tyrone.end_fill()
back()
up()
tyrone.forward(390)
down()
for i in range(103):
    tyrone.forward(3)
    tyrone.back(97)
    tyrone.right(1)
    tyrone.forward(100)
    tyrone.left(59)
tyrone.end_fill()
back()
up()
tyrone.backward(300)
down()
for i in range(1000):
    tyrone.right(random.randint(5,20))
    tyrone.forward(80)
    tyrone.back(random.randint(80,88))
    tyrone.forward(random.randint(1,8))
    tyrone.left(random.randint(5,20))
    
