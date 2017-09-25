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

