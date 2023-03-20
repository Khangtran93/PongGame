from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

# Create obeject screen to set up the screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('\t\tPong')
screen.tracer(0)

# Create right and left paddle objects
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

# Create ball object
ball = Ball()

# Pass the coordinates of right and left paddles
r_score = Score((50, 200))
l_score = Score((-50, 200))

# After all objects are created, call screen.listen() to listen to every
# press on the keyboard
screen.listen()
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

# Create boolean game_on to control the game
game_on = True

# Create the starting speed variable
speed = 0.1

# Game Start
while game_on:
    # Set the sleep rate to be equal to speed. The sleep rate is set to new speed value
    # for every loop
    time.sleep(speed)
    screen.update()
    # Object ball calls move() method
    ball.move()
    # if the ycor() and the ball is 290 or -290, meaning it hits the top or bottom wall, it bounces
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()
    # if the xcor() of the ball is greater than 350 and less than -350 (going out of bound), and the
    # the distance between the ball and paddle is less than 50, it bounces.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        # Everytime it hits the paddle, the speed will increase by decreasing speed value
        # (because the sleep rate is faster)
        if speed > 0.035:
            speed -= 0.01
    # If it go out of bound on the x direction, the ball's position will be reset and
    # the ball will move in the direction opposite from the one paddle just missed it.
    # The score will also increase.
    if ball.xcor() > 380:
        ball.reset_position()
        ball.move_y_amount*=-1
        ball.move_x_amount*=-1
        l_score.increase_score()
        speed = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        ball.move_y_amount *= -1
        ball.move_x_amount *= -1
        r_score.increase_score()
        speed = 0.1

screen.exitonclick()