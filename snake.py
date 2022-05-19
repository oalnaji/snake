POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(position)
            self.segments.append(seg)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # The range is going from (len(segments) -1) to 0 where each step is -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def grow(self):
        n_seg = Turtle("square")
        n_seg.color("white")
        n_seg.penup()

        n_x = self.segments[-1].xcor()
        n_y = self.segments[-1].ycor()
        n_seg.goto(n_x, n_y)

        self.segments.append(n_seg)



    def up(self):
        if self.segments[0] != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0] != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0] != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0] != RIGHT:
            self.segments[0].setheading(LEFT)