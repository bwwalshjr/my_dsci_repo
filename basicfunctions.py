#These are some examples of python-style function definitions.
import string

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
	
def word_counts(file_path, case_sensitive=True):
	text = open(file_path, 'r').read()
	if not case_sensitive:
		text = text.lower()
	text = text.translate(None, string.punctuation)
	
	word_dict = {}
	text = text.strip()
	for word in text.split():
		if not(word_dict.has_key(word)):
			word_dict[word] = 0
		word_dict[word] += 1
	return word_dict
		
#class word count function
def class_word_counts(file_path, case_sensitive = True, treat_punct_as_word = False, punct = ['!','.',',','"',"'",'?','~',]):
	text = open(file_path, 'r').read()
	if not case_sensitive:
		text = text.lower()
	#TODO: add code to count each punctuation character
	for p in punct:
		text = text.replace(p, ' ')
	words = text.split(' ')
	cleaned_words = []
	for w in words:
		if len(w) > 0:
			cleaned_words.append(w.strip())
	return histogram(cleaned_words)		

#Returns the largest element in thelist	
def my_max(elements):	
	if(len(elements) > 0):
		max = elements[0]
		for element in elements:
			max = element if element > max else max 
		return max
	return None
	
def variable_number_of_inputs(a, b,*rest):
	print("A is " + str(a))
	print("B is " + str(b))
	for e in rest:
		print("Next optional input: " + str(e))
		
		
#zip: reduces you a list of tuples
#map: pass in function and list, applies the function to each singular element
#filter: pass in function and list, filters out elements that don't match the function
#reduce: pass in function and list, applies computation to pairs of elements to return one element

def f_zip(f, *lists):
	return map(lambda tup: f(*tup), zip(*lists))
	
#recursive function to find sum from some number to another
def sum_range(start, end):
	if start == end:
		return end
	return sum_range(start, end-1) + end

#reverses list recursively 	
def rrev(list):
		return (list[-1] + rrev(list[:-1]) if list else [])
	
#Recursive fibonacci	
def fib(first, second, n):
	if n==1:
		return first
	if n==2:
		return second
	return fib(second, first+second, n-1)

#Faster recursive fibonacci, use memoization to avoid re-solving sub-problems
def fast_fib(first, second, n, cache={}):
	if n==1:
		return first
	if n==2:
		return second
	elif cache.has_key(n):
		return cache[n]
	else:
		val = fast_fib(first, second, n-1, cache) + fast_fib(first, second, n-2, cache)
		cache[n] = val
		return val

#all combinations of one value from each set
def cart_product(*sets):
	if len(sets) == 1:
		return map(lambda x: [x], sets[0])
	else:
		rest = cart_product(*sets[1:])
		combine = lambda x: map(lambda y: [x] + y, rest)
		return reduce(lambda x,y: x + y, map(combine, sets[0]))
	
#Finds all distinct combinations of k elements taken from elts	
def kcomb(elts, k):
	if len(elts) == k:
		return [elts]
	if k == 1:
		return map(lambda x: [x], elts)
	else: 
		partials = kcomb(elts[1:], k - 1)
		return map(lambda x: [elts[0]] + x, partials) + kcomb(elts[1:], k)

#Build a compositional pipe function - 
#builds a new function that applies the specified functions in sequence to an input		
def pipe(function_sequence):
	def applier(input):
		output = input
		for f in function_sequence:
			output = f(output)
		return output

#Regression: building a function that fits the data, in order to predict a value
#Regression and classification = supervised learning