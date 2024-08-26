from turtle import Turtle, Screen
from random import randint
t = Turtle()
t.shape("turtle")
colors = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'brown', 'orange']
t.speed("fastest")
oot=True
while oot:
    nice = colors[randint(0,len(colors)-1)]
    rice = randint(1,2)
    l = randint(0,300)
    t.width(10)
    t.color(nice)
    if rice == 1:
        t.rt(l)
        t.fd(30)
    if rice == 2:
        t.left(l)
        t.fd(30)

s = Screen()
s.exitonclick()
