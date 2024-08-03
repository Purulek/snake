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
        self.scren = turtle.Screen()

    def __call__(self):
        turtle.color("red")
        turtle.penup()
        turtle.home()
        turtle.pendown()

    def movment (self):
        i = 0
        while True:
            move = self.scren.textinput("kierunek", "give drictory")
            if move == "w":
                turtle.forward(15)
            elif move == "d":
                turtle.right(90)
                turtle.forward(15)
            elif move == "a":
                turtle.left(90)
                turtle.forward(15)
            else:
                turtle.bye()
                break
            




board = Board(400,90,'blue')
board()
palyer = Snake()
palyer()
palyer.movment()