import turtle
import time
t2 = turtle.Turtle()
t1 = turtle.Turtle()


class Board:
    def __init__(self,lenght,wide,coulor) -> None:
        self.length = lenght
        self.wide = wide
        self.coulor = coulor
        

    def __call__(self):
        
        t2.speed(0)
        t2.color(self.coulor)
        t2.penup()
        t2.setpos(-200, -200)
        t2.pendown()
        for _ in range (4):
            t2.forward(self.length)
            t2.left(self.wide)

        time.sleep(1)
        #turtle.(self.length)
class Snake:
    def __init__(self) -> None:
        self.screen = turtle.Screen()
        self.direction = ["sleep"] * 3
        self.screen.tracer()

    def __call__(self):
        t1.color("red")
        t2.color("white")
        t2.penup()
        t2.home()
        
        t2.pendown()
        
       
        
        

    def move(self):
        t1.speed(1)
        t1.forward(10)
        print("t1 forward")
        #print(t1.ycor())
        #print(t1.xcor())
        self.direction.append("forward") 
        if t1.ycor() >= 200 or t1.ycor() <= -200 or t1.xcor() >= 200 or t1.xcor() <= -200:
            print("You lose")
            for word in self.direction:
                print (word)
            turtle.bye()
            
        
        

    def go_left(self, dummy=None):
        t1.left(90)
        print("t1 - left")
        self.direction.append("left") 


    def go_right(self, dummy=None):
        t1.right(90)
        print("t1 right")
        self.direction.append("right") 


    def turnig (self):
        i = 0
         
        while i < 500:
              for action in self.direction :
                print (action)
                if action =="left" :
                    t2.left(90)
                elif action == "right":
                    t2.right(90)
                elif action == "forward":
                    t2.forward(10)
                elif action == "sleep":
                    pass
                self.screen.listen()
                self.screen.ontimer(self.move(),250)
                self.screen.onkey(self.go_left, "Left")
                self.screen.onkey(self.go_right, "Right")
                self.screen.onkey(turtle.bye, "Up")
                
                i +=1 



            
            
            
        

          




board = Board(400,90,'blue')
board()
palyer = Snake()
palyer()
palyer.turnig()







