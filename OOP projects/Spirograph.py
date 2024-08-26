from turtle import Turtle, Screen
from random import randint

s = Screen()
s.colormode(255)
t = Turtle()
t.shape("turtle")
nine=0
t.speed("fastest")
def nice():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    q = (r, g, b)
    return q
for _ in range (3600000):
    nine+=.1
    t.left(nine)
    t.circle(100,360)
    t.color(nice())



s.exitonclick()
