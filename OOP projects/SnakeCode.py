from turtle import Turtle, Screen
from random import randint

s = Screen()
nyet = 0
turtles = []
food = []


class Snake:

    def __init__(self):
        Turtles = None
        self.score = 0
        self.writer = []
        with open('SnakeFile.txt', 'r') as file:
            self.highscore = file.read()

    def start(self):
        global nyet, new_turtle, turtles
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.setx(nyet)
        nyet -= 20
        turtles.append(new_turtle)
        return new_turtle

    def move(self):
        global turtles
        for sing in range(len(turtles) - 1, 0, -1):
            newx = turtles[sing - 1].xcor()
            newy = turtles[sing - 1].ycor()
            turtles[sing].goto(newx, newy)
        turtles[0].fd(20)

    def feed(self):
        global turtles
        y = randint(-255, 255)
        x = randint(-255, 255)
        food[0].setx(x)
        food[0].sety(y)

    def make_food(self):
        global food
        new_turtle1 = Turtle("square")
        new_turtle1.penup()
        new_turtle1.color("red")
        food.append(new_turtle1)
        self.feed()
        return new_turtle1

    def writing(self):
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.speed("fastest")
        new_turtle.goto(x=-260, y=270)
        new_turtle.write(f"Score: {self.score}    High Score: {self.highscore}", False, "Left", font=('Times New Roman', 16, 'normal'))
        self.writer.append(new_turtle)

    def update_score(self):
        self.score += 1
        self.writer[0].clear()
        self.writer[0].write(f"Score: {self.score}    High Score: {self.highscore}", False, "Left", font=('Times New Roman', 16, 'normal'))

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open('SnakeFile.txt', 'w') as file:
                file.write(str(self.highscore))
        self.score = 0



