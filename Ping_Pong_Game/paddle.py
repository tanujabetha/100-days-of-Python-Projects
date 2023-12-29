from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)   
        self.speed("fastest")
    
    def upDirection(self):
        if self.ycor()<230:
            new_y = self.ycor()+20
            self.goto(self.xcor(),new_y)
    
    def downDirection(self):
        if self.ycor()>-230:
            new_y = self.ycor()-20
            self.goto(self.xcor(),new_y)