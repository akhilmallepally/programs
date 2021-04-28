from turtle import Turtle
from random import randint

kevin = Turtle()
kevin.color('blue')
kevin.shape('turtle')
kevin.penup()
kevin.goto(-150,90)
kevin.pendown()

don = Turtle()
don.color('pink')
don.shape('turtle')
don.penup()
don.goto(-150,70)
don.pendown()
brad = Turtle()
brad.color('green')
brad.shape('turtle')
brad.penup()
brad.goto(-150,50)
brad.pendown()
chin = Turtle()
chin.color('red')
chin.shape('turtle')
chin.penup()
chin.goto(-150,30)
chin.pendown()

for movement in range(100):
    kevin.forward(randint(1,10))
    brad.forward(randint(1,10))
    chin.forward(randint(1,10))
    don.forward(randint(1,10))