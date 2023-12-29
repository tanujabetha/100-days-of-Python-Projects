from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_value = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_value}", align="center", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score_value += 1
        self.update_scoreboard()
    
    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center", font=("Arial", 24, "normal"))
