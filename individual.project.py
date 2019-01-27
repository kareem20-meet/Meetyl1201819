from turtle import *
import random

class Ball(turtle):
	def __init__ (self, radius, color, dx, dy, x, y):
		turtle.__init__(self)
		turtle.penup()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.penup()
		self.speed(0)
		self.dx = dx/10
		self.dy = dy/10
		self.goto(x,y)
	

	def move (self, screen_widht, screen_height):






 mainloop()