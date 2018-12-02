from turtle import *
import random

class Ball(Turtle)
    def __init__(self,radius,color,speed)
        Turtle.__init__(self)
        self.shape("circle")
        self.shapsize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed) 

Ball1 = Ball(2,"red",7)
ball1.goto(30,5)
Ball2 = Ball(5,"yellow",7)

def check_collision(ball1, Ball2):

	D = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
	if D > ball1.radius + ball2.radius:
		print("Balls do not collide")
	if D <= 
		

	     




