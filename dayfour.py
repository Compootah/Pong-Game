from math import*
from tracemalloc import stop
from turtle import*
import turtle
import time

#Window Setup
wn = turtle.Screen()
wn.title("Pong Game by Roy")
wn.bgcolor("black") #Background colour
wn.setup(width=800, height=600) #Window size
wn.tracer(0) #Reduce lag apparantly.

#Paddle (left side)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.75)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle (right side)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.75)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#Middle Line
line = turtle.Turtle()
line.shape("square")
line.shapesize(stretch_len=0.5, stretch_wid=600)
line.color("dim gray")
line.penup()
line.goto(0, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(-350, 260)
pen.write("Player A: 0", align= "left", font=("Arial", 25, "normal"))
pen.goto(350, 260)
pen.write("Player B: 0", align= "right", font=("Arial", 25, "normal"))
pen.hideturtle()

#Score

score_a = 0
score_b = 10
tempscore = 0

#Functions
def paddle_a_up(): #Paddle on the left
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up(): #Paddle on the right
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

def print_score():
    pen.clear()
    pen.goto(-350, 260)
    pen.write("Player 1: {}".format(score_a), align= "left", font=("Arial", 25, "normal"))
    pen.goto(350, 260)
    pen.write("Player 2: {}".format(score_b), align= "right", font=("Arial", 25, "normal"))

#User Interface / Keyboard Biddings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game Loop
while True:
    wn.update()

    #Pause once reset. (A rare bug is that if the ball ever reaches (0, 0), the game will pause for 3 seconds.)
    if ball.xcor() == 0 and ball.ycor() == 0:
        print_score()
        pen.goto(0, 0)
        pen.write("3", align = "center", font = ("Arial", 50, "bold"))
        time.sleep(1)
        print_score()
        pen.goto(0, 0)
        pen.write("2", align = "center", font = ("Arial", 50, "bold"))
        time.sleep(1)
        print_score()
        pen.goto(0, 0)
        pen.write("1", align = "center", font = ("Arial", 50, "bold"))
        time.sleep(1)
        pen.clear()
        print_score()


    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking

    #Top and Bottom
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Right and Left
    if ball.xcor() > 390:
        score_a += 1
        print_score()
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        score_b += 1
        print_score()
        ball.goto(0, 0)
        ball.dx *= -1

    #Paddle and Ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
    elif (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
    
    #Game end
    if score_a == 11 or score_b == 11:
        if score_a > score_b:
            pen.clear()
            print_score()
            pen.goto(0, 0)
            pen.write("Player 1 Wins", align = "center", font = ("Arial", 50, "normal"))
        else:
            pen.clear()
            print_score()
            pen.goto(0, 0)
            pen.write("Player 2 Wins", align = "center", font = ("Arial", 50, "normal"))
        time.sleep(1)
        break

"""
color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill
done()

for i in range(0, 10, 2): #range(start, stop, step)
    if i > 2:
        continue #Continue send the control back to the beginnging of the loop.
    if i % 2 == 1:
        pass #Pass is used as a placeholder statement. It prevents code from executing in its scope.
    else:
        print(i)
"""