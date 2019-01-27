import Tkinter as tk
import tkSimpleDialog as simpledialog
import turtle
import time
import random
from ball import Ball, Virus, Food
#s = Sound() 
#s.read('sound.wav') 
#s.play()
#Then when ever you want to ask the user for input use this code
greeting = simpledialog.askstring("Game Mode", "Play Easy or Intermediate or Extreme?", parent=tk.Tk().withdraw())
if greeting == ("Extreme"):
	turtle.hideturtle()
	turtle.goto(-400,0)
	turtle.write("Welcome to Extreme mode!", move=False, align="left", font=("Arial", 50, "bold"))
	time.sleep(2)
	turtle.clear()
	turtle.write("50 points to win", move=False, align="left", font=("Arial", 50, "bold"))
	time.sleep(2)
	turtle.clear()
	turtle.tracer(0)
	print("got this far")
	turtle.bgpic("/home/student/Desktop/Meetyl1201819/aga(1).gif")
	number_of_BALLS = 35
	minimum_ball_radius = 5
	maximum_ball_radius = 70
	maximum_virus_radius = 5
	minimum_virus_radius = 5
	number_of_virus = 6
	minimum_ball_dx = -20
	maximum_ball_dx = 20
	minimum_ball_dy = -20
	maximum_ball_dy = 20
	balls =[]
	food = []
	viruses=[]

	soya = Ball(35,35,35,35,30, "black")
	running = True
	score = 0
	sleep = .0077
	scoret = turtle.clone()
	screen_width = turtle.getcanvas().winfo_width()//2
	screen_height = turtle.getcanvas().winfo_height()//2
	for i in range(number_of_BALLS):

		screen_random1_x = int(-screen_width+maximum_ball_radius)
		screen_random2_x = int(screen_width-maximum_ball_radius)
		random_x = random.randint(screen_random1_x,screen_random2_x)
		
		screen_random1_y = int(-screen_height+maximum_ball_radius)
		screen_random2_y = int(screen_height-maximum_ball_radius)
		random_y = random.randint(screen_random1_y,screen_random2_y)
		
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		while random_dx == 0:
			random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		while random_dy == 0:
			random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		radius = random.randint(minimum_ball_radius,maximum_ball_radius)

		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		

		ball = Ball(random_x, random_y, random_dx, random_dy, radius,color)
		balls.append(ball)
	for i in range(number_of_virus):

		screen_random1_x = int(-screen_width+maximum_virus_radius)
		screen_random2_x = int(screen_width-maximum_virus_radius)
		random_x = random.randint(screen_random1_x,screen_random2_x)
		
		screen_random1_y = int(-screen_height+maximum_virus_radius)
		screen_random2_y = int(screen_height-maximum_virus_radius)
		random_y = random.randint(screen_random1_y,screen_random2_y)


		

		virus = Virus(random_x, random_y, color)
		viruses.append(virus)


	def move_all_balls():
		print(screen_width, screen_height)
		for variable in range(number_of_BALLS):
			balls[variable].move(screen_width,screen_height)

	def check_collide(ball_a,ball_b):
		if ball_a == ball_b:
			return False
							#squareroot ( x2-x1 squared ) + ( y2-y1 squared)
		balls_distance = ((ball_a.xcor()-ball_b.xcor())**2 +(ball_a.ycor()-ball_b.ycor())**2)**0.5

		if balls_distance+10 <= (ball_a.radius+ball_b.radius):
			return True 
		else:
			return False

	def check_all_balls_collision():
		for ball_a in balls:
			for ball_b in balls:
				if check_collide(ball_a,ball_b) == True:
					radius1 = ball_a.radius
					radius2 = ball_b.radius
					random_x = random.randint(screen_random1_x,screen_random2_x)
					random_y = random.randint(screen_random1_y,screen_random2_y)
					random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
					while random_dx == 0:
						random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
					random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
					while random_dy == 0:
						random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
					radius = random.randint(minimum_ball_radius,maximum_ball_radius)
					color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

					if radius1 > radius2:
						ball_b.goto(random_x,random_y)
						ball_b.dx = random_dx
						ball_b.dy = random_dy
						ball_b.radius = radius
						ball_b.shapesize(ball_b.radius/10)
						ball_b.color = color
						ball_a.radius += 0.5
						ball_a.shapesize(ball_a.radius/10)
						
					elif radius1 < radius2:
						ball_a.goto(random_x,random_y)
						ball_a.dx = random_dx
						ball_a.dy = random_dy
						ball_a.radius = radius
						ball_a.shapesize(ball_a.radius/10)
						ball_a.color = color
						ball_b.radius+= 0.5
						ball_b.shapesize(ball_b.radius/10)
			for virus in viruses:
				if check_collide(virus, ball_a):
					ball_a.radius -= 2
					ball_a.shapesize(ball_a.radius/10)
					random_x = random.randint(-screen_width ,screen_width)
					random_y = random.randint(-screen_height,screen_height)
					virus.goto(random_x,random_y)
						
	def check_myball_collision():	
		global score , scoret		
		for ball in balls:
			random_x = random.randint(screen_random1_x,screen_random2_x)
			random_y = random.randint(screen_random1_y,screen_random2_y)
			random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
			while random_dx == 0:
				random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
			random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
			while random_dy == 0:
				random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
			radius = random.randint(minimum_ball_radius,maximum_ball_radius)
			color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
			if check_collide(soya,ball) == True:
				radius33 = soya.radius
				radius44 = ball.radius

				if radius33 < radius44:
					print("Game Over")
					return 	False
				else:
					soya.radius+= 2
					soya.shapesize(soya.radius/10)
					if score == 50:
						print('you win')
						scoret.pu()
						scoret.goto(0,250)
						scoret.clear()
						scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
						scoret.goto(0,50)
						scoret.write("YOU WIN!!!", align="center",font=("Arial", 100 ,"normal"))
						
					else:
						score+= 1
						scoret.pu()
						scoret.goto(screen_width-100, screen_height-50)
						scoret.clear()
						scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
						ball.goto(random_x,random_y)
						ball.dx = random_dx
						while ball.dx == 0:
							ball.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
						ball.dy = random_dy
						while ball.dy == 0:
							ball.dy = random.randint(minimum_ball_dy,maximum_ball_dy)
						ball.r = radius
						ball.shapesize(ball.r/10)
						ball.color = color
		return True

	def movearound(event):
		x1 = event.x - screen_width
		y1 = screen_height - event.y
		soya.goto(x1,y1)
	turtle.getcanvas().bind("<Motion>", movearound)
	turtle.listen()


	counter = 150

	while running == True:
		# if screen_width !=  int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
		screen_width = turtle.getcanvas().winfo_width() // 2
		screen_height = turtle.getcanvas().winfo_height() // 2
		move_all_balls()
		check_all_balls_collision()
		if counter == 0:
			if check_myball_collision() == False:
				running = False
				turtle.goto(0,0)
				turtle.write("Game Over",align="center",font=("Arial", 60, "normal"))
				print("YOU COLLIDED")
			#turtle.bye()
		else:
			counter -= 1
		turtle.update()
		time.sleep(sleep)

elif greeting == ("Easy"):
	#s = sound() 
	#s.read('sound.wav') 
	#s.play()
	turtle.hideturtle()
	turtle.goto(-400,0)
	turtle.write("Welcome to Easy mode!", move=False, align="left", font=("Arial", 50, "bold"))
	time.sleep(2)
	turtle.clear()
	turtle.write("55 points to win", move=False, align="left", font=("Arial", 50, "bold"))
	time.sleep(2)
	turtle.clear()
	turtle.tracer(0)
	print("got this far")
	turtle.bgpic("/home/student/Desktop/Meetyl1201819/work.gif")
	number_of_BALLS = 50
	minimum_ball_radius = 5
	maximum_ball_radius = 50
	number_of_food= 50
	number_of_virus = 15
	minimum_virus_radius = 3
	maximum_virus_radius = 3
	minimum_food_radius = 10
	maximum_food_radius = 10
	minimum_ball_dx = -3
	maximum_ball_dx = 3
	minimum_ball_dy = -3
	maximum_ball_dy = 3
	balls =[]
	foods = []
	viruses = []

	soya = Ball(30,30,30,34,20, "grey")
	running = True
	score = 0
	sleep = .0077
	scoret = turtle.clone()
	screen_width = turtle.getcanvas().winfo_width()//2
	screen_height = turtle.getcanvas().winfo_height()//2
	for i in range(number_of_BALLS):

		screen_random1_x = int(-screen_width+maximum_ball_radius)
		screen_random2_x = int(screen_width-maximum_ball_radius)
		random_x = random.randint(screen_random1_x,screen_random2_x)
		
		screen_random1_y = int(-screen_height+maximum_ball_radius)
		screen_random2_y = int(screen_height-maximum_ball_radius)
		random_y = random.randint(screen_random1_y,screen_random2_y)
		
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		while random_dx == 0:
			random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		while random_dy == 0:
			random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		radius = random.randint(minimum_ball_radius,maximum_ball_radius)

		color = (random.randint(0,255), random.randint(0,255), random.randint(0,250))
		

		ball = Ball(random_x, random_y, random_dx, random_dy, radius,color)
		balls.append(ball)

	for i in range(number_of_food):

		screen_random1_x = int(-screen_width+maximum_food_radius)
		screen_random2_x = int(screen_width-maximum_food_radius)
		random_x = random.randint(screen_random1_x,screen_random2_x)
		
		screen_random1_y = int(-screen_height+maximum_food_radius)
		screen_random2_y = int(screen_height-maximum_food_radius)
		random_y = random.randint(screen_random1_y,screen_random2_y)

		color = (random.randint(0,250), random.randint(0,255), random.randint(0,255))
		

		food = Food(random_x, random_y, color)
		foods.append(food)

	for i in range(number_of_virus):

		screen_random1_x = int(-screen_width+maximum_virus_radius)
		screen_random2_x = int(screen_width-maximum_virus_radius)
		random_x = random.randint(screen_random1_x,screen_random2_x)
		
		screen_random1_y = int(-screen_height+maximum_virus_radius)
		screen_random2_y = int(screen_height-maximum_virus_radius)
		random_y = random.randint(screen_random1_y,screen_random2_y)


		

		virus = Virus(random_x, random_y, color)
		viruses.append(virus)

	def move_all_balls():
		print(screen_width, screen_height)
		for variable in range(number_of_BALLS):
			balls[variable].move(screen_width,screen_height)

	def check_collide(ball_a,ball_b):
		if ball_a == ball_b:
			return False
							#squareroot ( x2-x1 squared ) + ( y2-y1 squared)
		balls_distance = ((ball_a.xcor()-ball_b.xcor())**2 +(ball_a.ycor()-ball_b.ycor())**2)**0.5

		if balls_distance+10 <= (ball_a.radius+ball_b.radius):
			return True 
		else:
			return False

	def check_all_balls_collision():
		for ball_a in balls:
			for ball_b in balls:
				if check_collide(ball_a,ball_b) == True:
					radius1 = ball_a.radius
					radius2 = ball_b.radius
					random_x = random.randint(screen_random1_x,screen_random2_x)
					random_y = random.randint(screen_random1_y,screen_random2_y)
					random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
					while random_dx == 0:
						random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
					random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
					while random_dy == 0:
						random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
					radius = random.randint(minimum_ball_radius,maximum_ball_radius)
					color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

					if radius1 > radius2:
						ball_b.goto(random_x,random_y)
						ball_b.dx = random_dx
						ball_b.dy = random_dy
						ball_b.radius = radius
						ball_b.shapesize(ball_b.radius/10)
						ball_b.color = color
						ball_a.radius += 0.5
						ball_a.shapesize(ball_a.radius/10)
						
					elif radius1 < radius2:
						ball_a.goto(random_x,random_y)
						ball_a.dx = random_dx
						ball_a.dy = random_dy
						ball_a.radius = radius
						ball_a.shapesize(ball_a.radius/10)
						ball_a.color = color
						ball_b.radius+= 0.5
						ball_b.shapesize(ball_b.radius/10)
			for food in foods:
				if check_collide(food, ball_a):
					ball_a.radius+= .2
					ball_a.shapesize(ball_a.radius/10)
					random_x = random.randint(-screen_width ,screen_width)
					random_y = random.randint(-screen_height,screen_height)
					food.goto(random_x,random_y)
			for virus in viruses:
				if check_collide(virus, ball_a):
					ball_a.radius-= 2
					ball_a.shapesize(ball_a.radius/10)
					random_x = random.randint(-screen_width ,screen_width)
					random_y = random.randint(-screen_height,screen_height)
					virus.goto(random_x,random_y)
	def check_myball_collision():	
		global score , scoret		
		for ball in balls:
			random_x = random.randint(-screen_width ,screen_width)
			random_y = random.randint(-screen_height,screen_height)
			random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
			while random_dx == 0:
				random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
			random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
			while random_dy == 0:
				random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
			radius = random.randint(minimum_ball_radius,maximum_ball_radius)
			color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
			if check_collide(soya,ball) == True:
				radius33 = soya.radius
				radius44 = ball.radius

				if radius33 < radius44:
					print("Game Over")
					return 	False
				else:
					soya.radius+= 2
					soya.shapesize(soya.radius/10)
					if score == 55:
						print('you win')
						scoret.pu()
						scoret.goto(0,250)
						scoret.clear()
						scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
						scoret.goto(0,50)
						scoret.write("YOU WIN!!!", align="center",font=("Arial", 100 ,"normal"))
						
					else:
						score+= .5
						scoret.pu()
						scoret.goto(screen_width-100, screen_height-50)
						scoret.clear()
						scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
						ball.goto(random_x,random_y)
						ball.dx = random_dx
						while ball.dx == 0:
							ball.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
						ball.dy = random_dy
						while ball.dy == 0:
							ball.dy = random.randint(minimum_ball_dy,maximum_ball_dy)
						ball.r = radius
						ball.shapesize(ball.r/10)
						ball.color = color
		for food in foods: 
			if check_collide(food, soya):
				soya.radius+= 1
				soya.shapesize(soya.radius/10)
				if score == 50:
					print('you win')
					scoret.pu()
					scoret.goto(0,250)
					scoret.clear()
					scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
					scoret.goto(0,50)
					scoret.write("YOU WIN!!!", align="center",font=("Arial", 100 ,"normal"))
				else:
					score+= 1
					scoret.pu()
					scoret.goto(screen_width-100, screen_height-50)
	     			scoret.clear()
	     			scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
	     			food.goto(random_x,random_y)
	     			food.color = color
		return True

	def movearound(event):
		x1 = event.x - screen_width
		y1 = screen_height - event.y
		soya.goto(x1,y1)
	turtle.getcanvas().bind("<Motion>", movearound)
	turtle.listen()


	counter = 150

	while running == True:
		# if screen_width !=  int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
		screen_width = turtle.getcanvas().winfo_width() // 2
		screen_height = turtle.getcanvas().winfo_height() // 2
		move_all_balls()
		check_all_balls_collision()
		if counter == 0:
			if check_myball_collision() == False:
				running = False
				turtle.goto(0,0)
				turtle.write("Game Over",align="center",font=("Arial", 60, "normal"))
				print("YOU COLLIDED")
			#turtle.bye()
		else:
			counter -= 1

		turtle.update()
		time.sleep(sleep)

elif greeting == ("Intermediate"):
	#s = Sound() 
	#s.read('/home/student/Desktop/Meetyl1201819/Motivating and Upbeat Background Music.mp3') 
	#s.play()
	turtle.hideturtle()
	turtle.goto(-450,0)
	turtle.write("Welcome to Medium mode!", move=False, align="left", font=("Arial", 50, "bold"))
	time.sleep(2)
	turtle.clear()
	turtle.write("150 points to win", move=False, align="left", font=("Arial", 50, "bold"))
	time.sleep(2)
	turtle.clear()
	turtle.tracer(0)
	print("got this far")
	turtle.bgpic("/home/student/Desktop/Meetyl1201819/work.gif")
	number_of_BALLS = 35
	minimum_ball_radius = 10
	maximum_ball_radius = 100
	number_of_food= 200
	minimum_food_radius = 10
	maximum_food_radius = 10
	minimum_ball_dx = -5
	maximum_ball_dx = 5
	minimum_ball_dy = -5
	maximum_ball_dy = 3
	balls =[]
	foods = []

	soya = Ball(30,30,30,34,20, "Blue")
	running = True
	score = 0
	sleep = .0077
	scoret = turtle.clone()
	screen_width = turtle.getcanvas().winfo_width()//2
	screen_height = turtle.getcanvas().winfo_height()//2
	for i in range(number_of_BALLS):

		screen_random1_x = int(-screen_width+maximum_ball_radius)
		screen_random2_x = int(screen_width-maximum_ball_radius)
		random_x = random.randint(screen_random1_x,screen_random2_x)
		
		screen_random1_y = int(-screen_height+maximum_ball_radius)
		screen_random2_y = int(screen_height-maximum_ball_radius)
		random_y = random.randint(screen_random1_y,screen_random2_y)
		
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		while random_dx == 0:
			random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		while random_dy == 0:
			random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		radius = random.randint(minimum_ball_radius,maximum_ball_radius)

		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		

		ball = Ball(random_x, random_y, random_dx, random_dy, radius,color)
		balls.append(ball)

	for i in range(number_of_food):

		screen_random1_x = int(-screen_width+maximum_food_radius)
		screen_random2_x = int(screen_width-maximum_food_radius)
		random_x = random.randint(screen_random1_x,screen_random2_x)
		
		screen_random1_y = int(-screen_height+maximum_food_radius)
		screen_random2_y = int(screen_height-maximum_food_radius)
		random_y = random.randint(screen_random1_y,screen_random2_y)

		

		food = Food(random_x, random_y, color)
		foods.append(food)

	def move_all_balls():
		print(screen_width, screen_height)
		for variable in range(number_of_BALLS):
			balls[variable].move(screen_width,screen_height)

	def check_collide(ball_a,ball_b):
		if ball_a == ball_b:
			return False
							#squareroot ( x2-x1 squared ) + ( y2-y1 squared)
		balls_distance = ((ball_a.xcor()-ball_b.xcor())**2 +(ball_a.ycor()-ball_b.ycor())**2)**0.5

		if balls_distance+10 <= (ball_a.radius+ball_b.radius):
			return True 
		else:
			return False

	def check_all_balls_collision():
		for ball_a in balls:
			for ball_b in balls:
				if check_collide(ball_a,ball_b) == True:
					radius1 = ball_a.radius
					radius2 = ball_b.radius
					random_x = random.randint(screen_random1_x,screen_random2_x)
					random_y = random.randint(screen_random1_y,screen_random2_y)
					random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
					while random_dx == 0:
						random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
					random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
					while random_dy == 0:
						random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
					radius = random.randint(minimum_ball_radius,maximum_ball_radius)
					color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

					if radius1 > radius2:
						ball_b.goto(random_x,random_y)
						ball_b.dx = random_dx
						ball_b.dy = random_dy
						ball_b.radius = radius
						ball_b.shapesize(ball_b.radius/10)
						ball_b.color = color
						ball_a.radius += 0.01
						ball_a.shapesize(ball_a.radius/10)
						
					elif radius1 < radius2:
						ball_a.goto(random_x,random_y)
						ball_a.dx = random_dx
						ball_a.dy = random_dy
						ball_a.radius = radius
						ball_a.shapesize(ball_a.radius/10)
						ball_a.color = color
						ball_b.radius+= 0.01
						ball_b.shapesize(ball_b.radius/10)
			for food in foods:
				if check_collide(food, ball_a):
					ball_a.radius+= .2
					ball_a.shapesize(ball_a.radius/10)
					random_x = random.randint(-screen_width ,screen_width)
					random_y = random.randint(-screen_height,screen_height)
					food.goto(random_x,random_y)
	def check_myball_collision():	
		global score , scoret		
		for ball in balls:
			random_x = random.randint(-screen_width ,screen_width)
			random_y = random.randint(-screen_height,screen_height)
			random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
			while random_dx == 0:
				random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
			random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
			while random_dy == 0:
				random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
			radius = random.randint(minimum_ball_radius,maximum_ball_radius)
			color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
			if check_collide(soya,ball) == True:
				radius33 = soya.radius
				radius44 = ball.radius

				if radius33 < radius44:
					print("Game Over")
					return 	False
				else:
					soya.radius+= 1.5
					soya.shapesize(soya.radius/10)
					if score == 50:
						print('you win')
						scoret.pu()
						scoret.goto(0,250)
						scoret.clear()
						scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
						scoret.goto(0,50)
						scoret.write("YOU WIN!!!", align="center",font=("Arial", 100 ,"normal"))
						
					else:
						score+= .5
						scoret.pu()
						scoret.goto(screen_width-100, screen_height-50)
						scoret.clear()
						scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
						ball.goto(random_x,random_y)
						ball.dx = random_dx
						while ball.dx == 0:
							ball.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
						ball.dy = random_dy
						while ball.dy == 0:
							ball.dy = random.randint(minimum_ball_dy,maximum_ball_dy)
						ball.r = radius
						ball.shapesize(ball.r/10)
						ball.color = color
		for food in foods: 
			if check_collide(food, soya):
				soya.radius+= 1
				soya.shapesize(soya.radius/10)
				if score == 150:
					print('you win')
					scoret.pu()
					scoret.goto(0,250)
					scoret.clear()
					scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
					scoret.goto(0,50)
					scoret.write("YOU WIN!!!", align="center",font=("Arial", 100 ,"normal"))
				else:
					score+= 1
					scoret.pu()
					scoret.goto(screen_width-100, screen_height-50)
	     			scoret.clear()
	     			scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
	     			food.goto(random_x,random_y)
	     			food.color = color
		return True

	def movearound(event):
		x1 = event.x - screen_width
		y1 = screen_height - event.y
		soya.goto(x1,y1)
	turtle.getcanvas().bind("<Motion>", movearound)
	turtle.listen()


	counter = 25

	while running == True:
		# if screen_width !=  int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
		screen_width = turtle.getcanvas().winfo_width() // 2
		screen_height = turtle.getcanvas().winfo_height() // 2
		move_all_balls()
		check_all_balls_collision()
		if counter == 0:
			if check_myball_collision() == False:
				running = False
				turtle.goto(0,0)
				turtle.write("Game Over",align="center",font=("Arial", 60, "normal"))
				print("YOU COLLIDED")
			#turtle.bye()
		else:
			counter -= 1

		turtle.update()
		time.sleep(sleep)