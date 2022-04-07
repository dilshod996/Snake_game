from turtle import Turtle

X_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]
        # be careful positioning of the code after create_snake() function

    def create_snake(self):
        for position in X_POSITION:
            self.add_part(position)

    def add_part(self, position):
        snake_name = Turtle(shape="square")
        snake_name.penup()
        snake_name.goto(position)
        snake_name.color("white")
        self.all_snakes.append(snake_name)
    def reset(self):
        for snake in self.all_snakes:
            snake.goto(1000,1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]

    def extend_snake(self):
        self.add_part(self.all_snakes[-1].position())

    def move(self):
        """To move snake"""
        for snake in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[snake - 1].xcor()
            new_y = self.all_snakes[snake - 1].ycor()
            self.all_snakes[snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
