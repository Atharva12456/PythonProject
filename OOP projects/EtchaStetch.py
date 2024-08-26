from turtle import Turtle, Screen
from random import randint
import colorgram
t = Turtle()
s = Screen()
s.colormode(255)
s.listen()
def away():
    t.fd(20)
def left():
    t.left(10)
def back():
    t.back(20)
def right():
    t.right(10)
s.onkey(key="green",fun=away)
s.onkey(key="a",fun=left)
s.onkey(key="s",fun=back)
s.onkey(key="d",fun=right)

s.exitonclick()
