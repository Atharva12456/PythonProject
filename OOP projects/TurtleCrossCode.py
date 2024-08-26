from turtle import Turtle, Screen
from random import randint


class CrossyRd(Turtle):
    def __init__(self):
        super().__init__()
        self.carshape = "square"
        self.mainturtle = []
        self.moveturt = -265
        self.movecar = 275
        self.colors = ["Yellow", "Cyan", "Red", "Light blue", "Pink", "Blue", "Purple", "Green", "Brown", "Orange",
                       "Lavender", "Teal", "Maroon", "Gold", "Slate Gray", "Salmon", "Indigo", "Turquoise", "Orchid",
                       "Coral", "Olive", "Sky Blue", "Tomato", "Sienna", "Steel Blue", "Thistle",
                       "Chocolate", "Plum"]
        self.cars = []
        self.move = 15
        self.level = 1
        self.writer = []
        self.h = 6
        self.highscore = 1

    def start(self):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.goto(0, self.moveturt)
        new_turtle.left(90)
        self.mainturtle.append(new_turtle)
        new_turtle.speed(10)
        self.writing()
        with open("TurtleCrossFile.txt", 'r') as f:
            self.highscore = f.read()
        return new_turtle

    def car(self):
        new_turtle = Turtle()
        new_yaxis = randint(a=-200, b=200)
        new_color = randint(0, len(self.colors) - 1)
        new_turtle.shape(self.carshape)
        new_turtle.penup()
        new_turtle.goto(self.movecar, new_yaxis)
        new_turtle.shapesize(.65, 1.5, 0)
        new_turtle.color(self.colors[new_color])
        new_turtle.speed("slow")
        self.cars.append(new_turtle)

    def up(self):
        self.mainturtle[0].fd(self.move)

    def down(self):
        self.mainturtle[0].bk(self.move)

    def new_level(self):
        self.level += 1
        self.writer[0].clear()
        self.writer[0].write(f"Level: {self.level}", False, "Left", font=('Times New Roman', 16, 'normal'))
        for i in self.cars:
            i.goto(1000, 1000)
            i.hideturtle()
            self.cars.remove(i)
        self.mainturtle[0].sety(self.moveturt)
        if self.h > 3:
            self.h -= 1

    def writing(self):
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.shape(self.carshape)
        new_turtle.penup()
        new_turtle.speed("fastest")
        new_turtle.goto(-270, 270)
        new_turtle.write(f"Level: {self.level}", False, "Left", font=('Times New Roman', 16, 'normal'))
        self.writer.append(new_turtle)

    def hs(self):
        if self.level > int(self.highscore):
            with open("TurtleCrossFile.txt", 'w') as f:
                f.write(str(self.level))
