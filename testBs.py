#This is a test driver for our functions defined in basicfunctions.py

#Import the module and name as bs
import basicfunctions as bs

#Test the add2 functions
print(bs.add2(3,5))
print(bs.add2(4,6))
print(bs.add2(5,7))

#Testing range function
print(bs.myRange(1,50))
print(bs.myRange(1,50,3))
print(bs.myRange(1, 50, increment = 4)) #Note that we can specify the optional argument inputs