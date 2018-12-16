from turtle import *
import random
import turtle
import math
class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed) 

ball1 = Ball(30,'red',10)
ball2 = Ball(20, 'blue',10)
balls =[]
balls.append(ball1)
balls.append(ball2)
ball1.goto(100,0)

def check_collision(ball1, Ball2):
	x2=ball1.xcor()
	y2=ball1.ycor()
	y1=ball2.xcor()
	y2=ball2.ycor()

	D = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
	if D > ball1.radius + ball2.radius:
		print('the balls did not collid')
	if D <= ball1.radius + ball2.radius:
		print('the balls collided')
check_collision(ball1,ball2)
def teleport():
	oldx1=ball.xcor()
	oldx2=ball.ycor()
	oldx2=ball.xcor()
	oldx1=ball.ycor()
	D = math.sqrt(math.pow((oldx2.oldx1),2) + math.pow((oldy2-oldx1),2))
	if D <= balls[1].radius +balls[0].radius:
		ball/goto(random.randint(1,100),random.randint(1,100))
	teleport()
	turtle.mainloop()

	     




