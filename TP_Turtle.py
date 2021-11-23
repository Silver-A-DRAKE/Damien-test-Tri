import turtle

maTortue=turtle.Turtle()

"""#Pour avancer :
maTortue.forward(50)

#Pour tourner :
maTortue.left(90)
maTortue.forward(50)

maTortue.right(90)
maTortue.forward(50)

#Pour régler la vitesse :
maTortue.speed(10)

#Pour régler la vitesse générale de toutes les tortues :
turtle.delay(0)

input()"""

#ex 1---------------------------------------------------------------------------------------
#1-cercle----------------
"""turtle.circle(100)
input()"""

#2-carré-----------------
"""maTortue.forward(50)

maTortue.left(90)
maTortue.forward(50)

maTortue.left(90)
maTortue.forward(50)

maTortue.left(90)
maTortue.forward(50)

maTortue.left(90)
maTortue.forward(50)
input()"""

#ex 2---------------------------------------------------------------------------------------
#1-escagot-cercle----------------
"""t = turtle.Turtle()
#r = taille du radius
r = 10
for i in range(100):
    t.circle(r + i, 45)"""

#2-escagot-carré-----------------
"""t = turtle.Turtle()
side = 200
for i in range(100):
   t.forward(side)
   t.right(90)
   side = side - 2"""

#ex 3---------------------------------------------------------------------------------------
#a-ligne-infini----------------
"""while 1:
    maTortue.forward(1)

input()"""

#b-déplacement-aléatoire-------
"""from turtle import *
import random

while 1:
    for i in range(100):
        angle = random.randint(-90, 90)
        forward(20)
        left(angle)

input()"""

#c-et-d-plusieurs-tortue------------
"""from turtle import *
import random
maTortue1=turtle.Turtle()
maTortue1.pencolor("red")
maTortue2=turtle.Turtle()
maTortue2.pencolor("blue")
maTortue3=turtle.Turtle()
maTortue3.pencolor("green")
while 1:
    maTortue1.forward(40)
    angle = random.randint(-90, 90)
    maTortue1.left(angle)
    maTortue2.forward(40)
    angle = random.randint(-90, 90)
    maTortue2.left(angle)
    maTortue3.forward(40)
    angle = random.randint(-90, 90)
    maTortue3.left(angle)

input()"""
#ex 4---------------------------------------------------------------------------------------
#-agare.io-------------------------
from turtle import *
import random
turtle.delay (0) 
maTortue1=turtle.Turtle()
maTortue1.pencolor("red")
maTortue2=turtle.Turtle()
maTortue2.pencolor("blue")
maTortue3=turtle.Turtle()
maTortue3.pencolor("green")

def postortue (tortue):
    X= random.randint(-300, 300)
    Y= random.randint(-300, 300)
    tortue.penup()
    tortue.goto(X,Y)
    tortue.pendown()

postortue(maTortue1)
postortue(maTortue2)
postortue(maTortue3)

while 1:
    maTortue1.forward(1)
    angle = random.randint(-50, 50)
    maTortue1.left(angle)
    maTortue2.forward(1)
    angle = random.randint(-50, 50)
    maTortue2.left(angle)
    maTortue3.forward(1)
    angle = random.randint(-50, 50)
    maTortue3.left(angle)

turtle.shapesize()