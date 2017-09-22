#These are some examples of python-style function definitions.

#Simple example: add two  numbers
def add2(x,y):
	return x + y
	
#Illustrate default arguments:
def myRange(start, end, increment=1):
	return range(start, end, increment)
	#Homework: rewrite this function to use a for loop
	rng = [start]
	start += 1
	while (start<end):
		rng.add(start)
		start += increment
	return rng
	
#Prints a triangle with side length and height n
def print_triangle(n, full=False):
	line_number = 1
	while(line_number <= n):
		print('*' * line_number)
		line_number += 1
		
	if(full):
		line_number -= 2
		while(line_number >= 1):
			print('*' * line_number)
			line_number -= 1
			
#Returns a histogram with item counts
def histogram(items):
	d = {}
	for item in items:
		if not(d.has_key(item)):
			d[item] = 0
		d[item] += 1
	return d