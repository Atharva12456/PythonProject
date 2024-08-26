import time
from turtle import Screen
import sys
from SnakeCode import Snake

s = Screen()
s.listen()
s.setup(600, 600)
s.tracer(0)
s.bgcolor("black")
s.title("Snake Game")
j = Snake()
turtles = []
turtles2 = []
food = []
gameOn = True
were = 0


def right():
    turtles[0].left(270)
    s.update()


def lt():
    turtles[0].left(90)
    s.update()


def up():
    turtles[0].left(0)
    s.update()


j.writing()
s.onkey(right, "Right")
s.onkey(up, "Up")
s.onkey(lt, "Left")
for begin in range(3):
    q = j.start()
    turtles.append(q)
    if were >= 1:
        turtles2.append(q)
    were += 1
po = j.make_food()
food.append(po)
while gameOn:
    for thy in turtles2:
        if turtles[0].distance(thy) < 25:
            print("You hit yourself and lost!")
            j.reset()
            sys.exit()
        if turtles[0].distance(food[0]) < 20:
            j.feed()
            j.start()
            j.update_score()
    if turtles[0].xcor() >= 285 or turtles[0].ycor() >= 285:
        print("Your Snake hit the edge and you lost!")
        j.reset()
        sys.exit()
    if turtles[0].xcor() <= -285 or turtles[0].ycor() <= -285:
        print("Your Snake hit the edge and you lost!")
        j.reset()
        sys.exit()

    j.move()
    s.update()
    time.sleep(.1)

s.exitonclick()
