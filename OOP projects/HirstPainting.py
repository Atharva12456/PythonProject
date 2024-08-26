from turtle import Turtle, Screen
from random import randint
import colorgram

s = Screen()
s.colormode(255)
t = Turtle()
t.shape("turtle")
t.width(20)
t.speed("fastest")
def nice():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    q = (r, g, b)
    return q
niet = 1
for hi in range(10):
    for dot in range(0,10):
        t.color(nice())
        t.fd(1)
        t.penup()
        t.fd(50)
        t.pendown()
        t.fd(1)
    if niet%2==0:
            t.right(90)
            t.penup()
            t.fd(50)
            t.right(90)
            t.pendown()
            t.fd(1)
    else:
            t.left(90)
            t.penup()
            t.fd(50)
            t.left(90)
            t.pendown()
            t.fd(1)
    niet+=1


s.exitonclick()
