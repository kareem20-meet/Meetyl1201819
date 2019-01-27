from turtle import *
import random
import math
class Ball(Turtle):
	def __init__ (self, radius, color, speed, dx, dy, x, y):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.penup()
		self.speed(0)
		self.dx = dx/10
		self.dy = dy/10
		self.goto(x,y)
		self.speed(speed)

	def move (self):
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + self.dx
		newy = oldy + self.dy
		self.goto(newx, newy)
		if(newx > 400 or newx < -400):
			self.dx = self.dx *-1
		if(newy > 400 or newy < -400):
			self.dy = self.dy*-1



ball = Ball(10,"blue",2,8,8,100,100)
ball1 = Ball(10,"black",2,7,9,-100,-100)


def check_collision(ball1, ball):
	radius_len = ball.radius + ball1.radius
	D = math.sqrt((ball.xcor() - ball1.xcor())**2 + (ball.ycor()-ball1.ycor()**2))
	if(radius_len > D):
		return True
	return False
while True:
 	if(check_collision(ball,ball1)):

 		tempx = ball1.dx
 		tempy = ball1.dy
 		ball.dx = ball.dx
 		ball.dy = ball.dy
 		ball.dx = tempx
 		ball.dy = tempy

mainloop()