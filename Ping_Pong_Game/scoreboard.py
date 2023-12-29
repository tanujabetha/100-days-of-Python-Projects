from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,"center",font=("ariel",12,"normal"))
        self.goto(100,200)
        self.write(self.r_score,"center",font=("ariel",12,"normal"))
        
        
    def l_point(self):
        self.l_score +=1
        self.updateScoreBoard()
        
    def r_point(self):
        self.r_score +=1
        self.updateScoreBoard()
        
    def checkScores(self,finalScore):
        if self.l_score == finalScore:
            return True
        elif self.r_score == finalScore:
            return True
    

            
            