#Ping Pong application 
#scripted by:
#Eng/Kirollos Gerges

#import turtle module 
import turtle 

wind =turtle.Screen() #initialize Screen 
wind.title("Ping pong") #set the title of the window
wind.bgcolor("black")#set Background color of window
wind.setup(width=800,height=600) #set up width and height of the window
wind.tracer(0) #stops the window from updating automatically

#madrab1 
madrab1 = turtle.Turtle() #initialize turtle object 
madrab1.speed(0) #set speed of animation 
madrab1.shape("square") #set the shape of the object 
madrab1.color("blue") #set the color of the shape 
madrab1.shapesize(stretch_wid=7.5,stretch_len=1) #stretch the shape 
madrab1.penup() #stops object from drawing lines 
madrab1.goto(-350,0) #set position of the object

#madrab2
madrab2 = turtle.Turtle() #initialize turtle object 
madrab2.speed(0) #set speed of animation 
madrab2.shape("square")#set the shape of the object 
madrab2.color("red")#set the color of the shape 
madrab2.shapesize(stretch_wid=7.5,stretch_len=1) #stretch the shape 
madrab2.penup() #stops object from drawing lines 
madrab2.goto(350,0) #set position of the object

#ball
ball = turtle.Turtle() #initialize turtle object 
ball.speed(0) #set speed of animation 
ball.shape("circle") #set the shape of the object 
ball.color("white") #set the color of the shape 
ball.penup() #stops object from drawing lines 
ball.goto(0,0)#set position of the object
ball.dx = 0.6 #rate of motion 0.2 pixel on screen
ball.dy = 0.6 #rate of motion 0.2 pixel on screen

#score 
score1=0
score2=0
score =turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player_1: 0              Player_2: 0",align="center",font="Arial,36,normal")





#functions
def madrab1_up():
    y=madrab1.ycor() #set y coordinates
    y+=20 #set y to increase by 20
    madrab1.sety(y)#set the y to the new y coordinate

def madrab1_down():
    y=madrab1.ycor() #set y coordinates
    y-=20 #set y to decrese by 20
    madrab1.sety(y)#set the y to the new y coordinate

def madrab2_up():
    y=madrab2.ycor() #set y coordinates
    y+=20 #set y to increase by 20
    madrab2.sety(y)#set the y to the new y coordinate

def madrab2_down():
    y=madrab2.ycor() #set y coordinates
    y-=20#set y to decrese by 20
    madrab2.sety(y)#set the y to the new y coordinate
 




#keyboard Bindings
wind.listen() #listen windowa
wind.onkeypress(madrab1_up,"w")#permit madrab1 toward when the user click w
wind.onkeypress(madrab1_down,"s")#permit madrab1 toward when the user click s
wind.onkeypress(madrab2_up,"Up")#permit madrab2 toward when the user click Up
wind.onkeypress(madrab2_down,"Down")#permit madrab12 toward when the user click Down


#main game loop 
while True:
    wind.update() #updates the screen everytime the loop run 

#move the ball
    ball.setx(ball.xcor()+ball.dx) #ball starts at 0 and everytime loops run-->+0.2
    ball.sety(ball.ycor()+ball.dy) #ball starts at 0 and everytime loops run-->+0.2

#border check ,top border +300px ,bottom border -300 px,ball is 20px
    if ball.ycor()>290: #if ball is at top border 
             ball.sety(290) #set y coordiinate +290
             ball.dy *=-1  #reverse direction , making +0.2--->-0.2
            
           

    if ball.ycor()<-290:#if ball is at bottom border 
             ball.sety(-290) #set y coordiinate -290
             ball.dy *=-1 #reverse direction , making +0.2--->-0.2

    if ball.xcor()>390:    #if ball is at right border 
             ball.setx(390) #set x coordiinate -390
             ball.dx*=-1  #reverse direction , making +0.2--->-0.2
             score1=score1+1
             score.clear()
             score.write("Player_1: {}              Player_2: {}".format(score1,score2),align="center",font="Arial,36,normal")

    if ball.xcor()<-390:     #if ball is at left border 
             ball.setx(-390)   #set x coordiinate -390
             ball.dx*=-1      #reverse direction , making +0.2--->-0.2
             score2=score2+1
             score.clear()
             score.write("Player_1: {}              Player_2: {}".format(score1,score2),align="center",font="Arial,36,normal")

             #5abta madrab bal ball

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40):
            ball.setx(340)
            ball.dx *=-1  
            
             

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<madrab1.ycor()+40 and ball.ycor()>madrab1.ycor()-40):
            ball.setx(-340)
            ball.dx *=-1  
             

    
    
    
    
    
