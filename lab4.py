class Animal(object):
	def __init__(self,sound,name,age,favorite_color): 
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!! " + self.name + "is eatting" + food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self):
		print(self.name + " says " + self.sound)
cat = Animal("Meow" , "Max", "3" ,"blue")
cat.description()
cat.make_sound()
cat.eat("fish")

class Person(object):
	def __init__(self,name,gender,color_eye):
		self.sound = sound
		self.name = name
		self.gender = gender
		self.color_eye = color_eye
	def breakfast(self):
		print("I " + "," + self.name + " eat my favoritte food everyday! ")
	def sports(self):
		print(self.name + " loves to play football")
person =Person("Ali", "male", "blue")
person.breakfast()
person.sports()