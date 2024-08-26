from turtle import Turtle, Screen
from random import randint

t = Turtle()
t.shape("turtle")
colors = ["blue", "red", "orange", "green", "yellow", "gold"]
oof = True
nivce = 3
while oof:
    # if nivce == 11:
    #     oof = False
    ooga = colors[randint(0, len(colors) - 1)]
    t.color(ooga)
    angle = 360 / nivce
    for j in range(0, nivce):
        t.fd(100)
        t.left(angle)
    nivce += 1
def nice():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    q = (r, g, b)
    return q

for oof in range(200):
    t.color(nice())
s = Screen()
s.exitonclick()
