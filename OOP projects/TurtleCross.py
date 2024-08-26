import sys
import time
from turtle import Screen
from TurtleCrossCode import CrossyRd
from random import randint

s = Screen()
q = CrossyRd()
s.tracer(0)
s.setup(600, 600)
s.listen()
s.onkey(q.up, 'Up')
s.onkey(q.down, 'Down')
r = 0
q.start()
ooga = True
for i in range(10):
    q.car()
while ooga:
    r += 1
    if r == q.h:
        q.car()
        r = 0
    for l in q.cars:
        if q.mainturtle[0].ycor() >= 300:
            q.new_level()
            q.reset()
        if q.mainturtle[0].distance(l) < 20:
            q.hs()
            print(f"Your Turtle crashed on level {q.level}. Your highest level is level {q.highscore}.")
            q.reset()
            sys.exit(0)
        l.bk(randint(0, 20))
        if l.xcor() <= -300:
            l.goto(1000, 1000)
            l.hideturtle()
            q.cars.remove(l)
            q.car()

    s.update()
    time.sleep(0.1)

s.exitonclick()
