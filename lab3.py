'''
import turtle 
turtle.forward(150)
turtle.right(135)
turtle.forward(150)
turtle.right(135)
turtle.forward(150)
turtle.right(135)
turtle.forward(150)
turtle.right(135)
turtle.forward(100)
turtle.begin_fill()
turtle.mainloop                       
'''

'''
import turtle 
def square():
	for i in range(4):
	    turtle.forward(100)
	    turtle.left(90)
turtle.begin_fill()
square()
turtle.right(45)
turtle.forward(90)
turtle.left(100)
turtle.forward(90)
turtle.end_fill()
turtle.mainloop
'''

import turtle
turtle.speed(0)
turtle.tracer(100)
while True:
	turtle.left(0.3)
	turtle.pendown()
	turtle.forward(100)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.goto(0,0)
turtle.mainloop()