import turtle
import time
import random
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
        t1.color("red")
        t2.color("white")
        t2.penup()
        t2.home()
        
        t2.pendown()
    
class Snake:
    def __init__(self) -> None:
        self.screen = turtle.Screen()
        self.fruit =turtle.Turtle()
        
        self.coordinates = []
        self.direction_of_t2 = ["sleep"] *5
        self.direction_of_t1 =["forward"] 
        self.screen.tracer()
        t1.shape("triangle")

        
    def treat(self):
        self.fruit.shape("circle")
        self.fruit.color("white")
        self.fruit.penup()
        xcor = random.randrange(-200,200, 10)
        ycor = random.randrange(-200,200, 10)
        self.fruit.setpos(xcor,ycor)
        self.fruit.pendown()
        self.fruit.color("orange")
       
        
        

    def move(self):
        t1.speed(1)
        t1.forward(10)
        self.coordinates.append([t1.xcor(),t1.ycor()])
        self.direction_of_t2.append("forward") 
        self.ouroboros()
        if t1.ycor() >= 200 or t1.ycor() <= -200 or t1.xcor() >= 200 or t1.xcor() <= -200:
            print("You lose")
            turtle.bye()
        elif abs(t1.ycor()) >= abs(self.fruit.ycor())-1 and abs(t1.ycor()) <= abs(self.fruit.ycor())+ 1 and abs(t1.xcor()) >= abs(self.fruit.xcor()) -1 and abs(t1.xcor()) <= abs(self.fruit.xcor()) + 1 :
            self.direction_of_t2.append("sleep")
            self.direction_of_t2.append("sleep")
            self.fruit.color("white")
            
    def ouroboros(self):
        waiting = [ sleep for sleep in self.direction_of_t2 if sleep == "sleep"]
        self.coordinate = self.coordinates[- len(waiting):]
        self.cords = self.coordinate.pop()
        for cords in self.coordinate:
            if (t1.ycor()) >= (cords[1])-1 and (t1.ycor()) <= (cords[1])+ 1 and t1.xcor() >= (cords[0]) -1 and (t1.xcor()) <= (cords[0]) + 1 :
                print("you lose")
                turtle.bye()
        self.coordinate.append(self.cords)
       
        #adding into list next movment
    def left(self):
        index =self.loop + 1
        self.direction_of_t1.insert(index,  "left")

    
    def right(self):
        index =self.loop + 1
        self.direction_of_t1.insert(index,  "right")

    
    def forward(self):
        self.direction_of_t1.append("forward")





    #moving Function
    def go_left(self, dummy=None):
        t1.left(90)
        self.direction_of_t2.append("left") 
        print("going to the left")

    def go_right(self, dummy=None):
        t1.right(90)
        self.direction_of_t2.append("right")
        print("going to the right")


    




    def turnig (self):
        self.loop = 0
         
        while self.loop < 1:
              
            for action_of_t1, action_of_t2 in zip(self.direction_of_t1 ,self.direction_of_t2) :
            

                if len(self.direction_of_t1) % 40 == 0:
                    self.treat()
                if action_of_t2 =="left" :
                    t2.left(90)
                elif action_of_t2 == "right":
                    t2.right(90)
                elif action_of_t2 == "forward":
                    t2.forward(10)
                elif action_of_t2 == "sleep":
                    pass

                self.screen.listen()
                self.screen.onkey(self.left, "Left")
                self.screen.onkey(self.right, "Right")
                
                self.screen.ontimer(self.forward(),350)
                if action_of_t1 == "forward":
                    self.screen.ontimer(self.move(),350)
                elif action_of_t1 == "left":
                    self.go_left()
                elif action_of_t1 == "right":
                      self.go_right()
                

              
                  
                
                self.loop +=1 
              
                

                



            
            
            
        

          




board = Board(400,90,'blue')
board()
palyer = Snake()

palyer.turnig()







