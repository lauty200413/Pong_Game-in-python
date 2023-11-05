from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


scoreboard = Scoreboard()
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()


screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()
