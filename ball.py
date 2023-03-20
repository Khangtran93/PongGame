from turtle import Turtle

# Class Ball inherits from class Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.penup()
        self.move_x_amount = 10
        self.move_y_amount = 10

    # Method move() is called in main for every loop and it sets the new_y and new_x to
    # be the previous coordinates plus the move_amount of both x and y direction.
    def move(self):
        new_y = self.ycor() + self.move_y_amount
        new_x = self.xcor() + self.move_x_amount
        self.goto(new_x, new_y)

    # When a bounce is called, it changes the direction of either x or y direction
    def bounce_y(self):
        self.move_y_amount *= -1

    def bounce_x(self):
        self.move_x_amount *= -1

    # Reset position by calling goto(0,0) (center)
    def reset_position(self):
        self.goto(0, 0)
