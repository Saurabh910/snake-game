from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    # Create Starting Snake
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for p in POSITIONS:
            self.segment_addition(p)

    def segment_addition(self, positions):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(positions)
        self.segments.append(segment)

    def extend(self):
        extend_position = self.segments[-1].position()
        POSITIONS.append(extend_position)
        self.segment_addition(extend_position)

    # Move the snake forward
    def move_forward(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            next_cord = POSITIONS[seg_num-1]
            self.segments[seg_num].goto(next_cord)
            POSITIONS[seg_num] = self.segments[seg_num].position()
        self.head.forward(MOVE)
        POSITIONS[0] = self.head.position()

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(DOWN)
