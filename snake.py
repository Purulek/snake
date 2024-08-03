import turtle
import time

class Board:
    def __init__(self,lenght,wide,coulor) -> None:
        self.length = lenght
        self.wide = wide
        self.coulor = coulor
        

    def __call__(self):
        
        
        turtle.color(self.coulor)
        turtle.penup()
        turtle.setpos(-200, -200)
        turtle.pendown()
        for _ in range (4):
            turtle.forward(self.length)
            turtle.left(self.wide)

        time.sleep(1)
        #turtle.(self.length)
class Snake:
    def __init__(self) -> None:
        self.screen = turtle.Screen()

    def __call__(self):
        turtle.color("red")
        turtle.penup()
        turtle.home()
        turtle.pendown()

    def move(self):
        turtle.forward(15)
        

    def go_left(dummy=None):
        turtle.left(90)


    def go_right(dummy=None):
        turtle.right(90)


    def turnig (self):
        i = 0
        
        while i < 50:
            self.screen.listen()
            self.screen.onkey(self.go_left, "Left")
            self.screen.onkey(self.go_right, "Right")   
            self.screen.ontimer(self.move(),250)
            i += 1
        

          




board = Board(400,90,'blue')
board()
palyer = Snake()
palyer()
palyer.turnig()







