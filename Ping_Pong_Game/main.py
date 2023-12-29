from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
import random as rd

#Screen settings
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong!")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
r_paddle.speed("fastest")
r_paddle.speed("fastest")
# dottedTurtle = Turtle()
score = ScoreBoard()
ball = Ball()
l_win = False
r_win = False
#Asking the user for the score they are playing for
userBet = screen.textinput(
    "Make Score", "What is the score you are playing for?"
)
userBet = int(userBet)

#Listening to the keys pressed by the user
screen.listen()
screen.onkey(r_paddle.upDirection,"Up")
screen.onkey(r_paddle.downDirection,"Down")
#"w" for left movement up
#"s" for left movement down
screen.onkey(l_paddle.upDirection," w")
screen.onkey(l_paddle.downDirection,"s")
game_is_on = False
randomSpeed = 0
while not game_is_on:
    time.sleep(ball.ballSpeed)
    screen.update()
    ball.move()
    #Detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #Detect collision with paddle
    if(ball.distance(r_paddle)<50 and ball.xcor()>307) or (ball.distance(l_paddle)<50 and ball.xcor()<-307):
        ball.bounce_x()

    #Paddle missing the ball by right 
    if(ball.xcor()>380):
        ball.reset_position()
        score.l_point()
        game_is_on = score.checkScores(userBet)
        if game_is_on:
            l_win = True
    
    #Paddle missing the ball by left   
    if(ball.xcor()<-380):
        ball.reset_position()
        score.r_point()  
        game_is_on = score.checkScores(userBet)
        if game_is_on: 
            r_win = True
            
            
    #Checking the winner:
if r_win:
    score.goto(0,0)
    score.write(f"Congratulations! The right player won!!",align="center", font=("Arial", 24, "normal"))
else:
    score.goto(0,0)
    score.write(f"Congratulations! The left player won!!",align="center", font=("Arial", 24, "normal"))
screen.exitonclick()  
