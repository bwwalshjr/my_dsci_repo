print("Hello World!")

e1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
e2 = [(1, 'a'), (2,'b'), (3,'c'), (4,'d'), (5,'e')]

#Print out elements in a list of strings
for char in e1:
	print('Next character: ' + char)

#Print two blank lines	
print("\n\n")	
	
#Print out elements in list of tuples - each field separately
for (number,letter) in e2:
	print("The number is: " + str(number))
	print("The letter is: " + letter)
	print('____________')
	
#Print two blank lines	
print("\nSame as above but a different way:\n")	

#Prints out elements in list of tuples, but by referencing tuple positions
for tuple in e2:
	print("The number is: " + str(tuple[0]))
	print("The letter is: " + tuple[1])
	print('____________')
