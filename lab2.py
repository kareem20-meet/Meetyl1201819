67
a = [5 ,10,15,20,25]
def list():
	y = [a[0],a[-1]]
	print(y)
list()

a = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]
def l(a):
	for n in range(len(a)):
		if a[n] < 5 :
			print(a[n])

	l(a)
	
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]	
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def sadiq(a):
	for i in range (len(a)):
			for i in range (len(b)):
				if a[i] in a and b[i]:
					return i 