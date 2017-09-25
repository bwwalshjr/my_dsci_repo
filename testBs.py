#This is a test driver for our functions defined in basicfunctions.py

#Import the module and name as bs
import basicfunctions as bs
import string

#Test the add2 functions
#print(bs.add2(3,5))
#print(bs.add2(4,6))
#print(bs.add2(5,7))

#Testing range function
#print("My range: " + str(bs.myRange(1,50)))
#print("Py range: " + str(range(1,50)))
#print("My range: " + str(bs.myRange(1,50,3)))
#print("Py range: " + str(range(1,50,3)))
#print("My range: " + str(bs.myRange(1, 50, increment = 4))) #Note that we can specify the optional argument inputs
#print("Py range: " + str(range(1,50,4)))

#Test the triangle printing function
#bs.print_triangle(3)
#print("\n")
#bs.print_triangle(5)
#print("\n")
#bs.print_triangle(5,full=True)

#Tests histogram function
#print(bs.histogram(['a','x', 2, 'x', 3, 2]))
#print(bs.histogram(['1','2','2','3','3','3','a','b','c','c']))

#Tests file reading histogram function
print(bs.word_counts('C:\GitHub\my_dsci_401\data\sample_text.txt', case_sensitive=True))
#print(bs.class_word_counts('C:\GitHub\my_dsci_401\data\sample_text.txt', case_sensitive=True))
