from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    def create_snake(self):
        x = 0
        y = 0
        for i in range(0, 3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            self.turtles.append(new_turtle)
            new_turtle.goto(x, y)
            x -= 20
    def move(self):
        for segment in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[segment - 1].xcor()
            new_y = self.turtles[segment - 1].ycor()
            self.turtles[segment].goto(new_x, new_y)
        self.turtles[0].fd(20)
    def up(self):
        if self.turtles[0].heading() != 270:
          self.turtles[0].setheading(90)
    def down(self):
        if self.turtles[0].heading() != 90:
          self.turtles[0].setheading(270)
    def right(self):
        if self.turtles[0].heading() != 180:
          self.turtles[0].setheading(0)
    def left(self):
        if self.turtles[0].heading() != 0:
          self.turtles[0].setheading(180)

    def extend(self):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        self.turtles.append(new_turtle)


