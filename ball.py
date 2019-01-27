from turtle import *
from turtle import Turtle
import random
colormode(255)
class Ball(Turtle):
	def __init__ (self,x,y,dx, dy, radius, color):
		Turtle.__init__(self)
		self.penup()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(0)
		self.dx = dx
		self.dy = dy
		self.goto(x,y)
	

	def move (self, screen_width, screen_height):
		current_x = self.xcor()
		current_y = self.ycor()
		newx = current_x + self.dx
		newy = current_y + self.dy
		right_side = newx + self.radius
		left_side = newx - self.radius
		bottom_side = newy - self.radius
		upper_side = newy + self.radius


 		

		if upper_side > screen_height or bottom_side < -screen_height:
			self.dy *= -1
			print("turn x")
		if right_side > screen_width or left_side < -screen_width:
			self.dx *= -1
			print("turn y")

		self.goto(newx, newy)



class Hexagon(Turtle):
 	def __init__(self, x):
 		Turtle.__init__(self)
 		turtle.register_shape("Hexagon",((0,0),(x,0),(2*x,x),(2*x,2*x),(x,3*x),(0,3*x),(-x,2*x),(-x,x),(0,0)))
 		self.shape("Hexagon")
 		self.color("green")



class Food(Ball):
	def __init__ (self,x,y, color):
		Turtle.__init__(self)
		self.penup()
		self.shape("circle")
		self.shapesize(.5)
		self.radius =.5
		self.color("black")
		self.goto(x, y)

class Rectangle(Turtle):
	def __init__ (self,x,y):
		Turtle.__init__(self)
		turtle.register_shape("rectangle",((0,0),(0,0),(0,0),(0,0),(0,0)))
		self.shape("rectangle")
		self.color("green")

class Square(Rectangle):
	def __init__ (self):
		Rectangle.__init__(self,50,50)

class Virus(Ball):
	def __init__ (self,x,y, color):
		Turtle.__init__(self)
		self.penup()
		self.shape("circle")
		self.shapesize(3)
		self.radius =3
		self.color("green")
		self.goto(x, y)


# mainloop()



