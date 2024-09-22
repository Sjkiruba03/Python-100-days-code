from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.update_segment(position)

    def update_segment(self, position):
        tommy = Turtle(shape="square")
        tommy.up()
        tommy.color("white")
        tommy.goto(position)
        self.segments.append(tommy)

    def extend_segment(self):
        self.update_segment(self.segments[-1].position())

    def move(self,):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



