from turtle import Turtle

# Class Score inherits from class Turtle
class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update()

    # method update will update everytime method increase_score is called. It will write the new
    # value of the score belongs to that object (l_score or r_score)
    def update(self):
        self.write(f"{self.score}", move=False, align='center', font=('Courier', 50, 'normal'))

    # Method increase_score increment the score, clear the screen and call update method to write
    # to the screen again
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()