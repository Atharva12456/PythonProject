
from turtle import Turtle, Screen
from random import randint

s = Screen()
blue = Turtle()
red = Turtle()
green = Turtle()
orange = Turtle()
pink = Turtle()
yug2 = input("Who do you think is going to win (blue,red,orange,green,pink)?: ").lower()
tur = [blue, red, green, orange, pink]
colors = ["blue", "red", "green", "orange", "pink"]
oof = True
niete = -80
yug = 0
def start(b):
    global niete
    b.penup()
    b.setx(-430)
    b.sety(niete)
    niete += 40
for j in tur:
    j.shape("turtle")
    j.color(colors[yug])
    yug += 1
    start(j)
while oof:
    for j in tur:
        j.speed("fastest")
        l = randint(0, 20)
        j.fd(l)
        p = j.xcor()
        if p >= 459:
             if yug2 == j.pencolor():
                print(f"{j.pencolor()} is the winner! You got it right!")
                oof = False
             else:
                print(f"{j.pencolor()} is the winner! You got it wrong.")
                oof=False


s.exitonclick()
