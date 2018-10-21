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