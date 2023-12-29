from turtle import Turtle, Screen
#Width of 20, height of 20, x_pos =0, y_pos = 0
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.ballSpeed = 0.1
         
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    #Bouncing in the y axis
    def bounce_y(self):
        self.y_move *=-1
        
    #bouncing x axis
    def bounce_x(self):
        self.x_move *=-1
        self.ballSpeed *= 0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.ballSpeed = 0.1
        self.bounce_x()
        

        
        