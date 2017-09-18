#These are some examples of python-style function definitions.

#Simple example: add two  numbers
def add2(x,y):
	return x + y
	
#Illustrate default arguments:
def myRange(start, end, increment=1):
	return range(start, end, increment)
	#Homework: rewrite this function to use a for loop