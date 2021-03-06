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
#print(bs.word_counts('C:\GitHub\my_dsci_401\data\sample_text.txt', case_sensitive=True))
#print(bs.class_word_counts('C:\GitHub\my_dsci_401\data\sample_text.txt', case_sensitive=True))

#Tests my max function
#print(bs.my_max([2,4,23,5,2,1,6,9,3,2]))
#print(bs.my_max([]))

#Test variable number of inputs
#bs.variable_number_of_inputs(1,2,3,4,5,6,7,'fuck','you')

#Test fzip
#list_a = [1,2,3]
#list_b = [4,5,6]
#print(bs.f_zip((lambda x,y: x+y), list_a, list_b))
#print(bs.f_zip(max, [1,2,3], [4,5,6], [7,8,9]))

#Test recursive sum_range
#print(bs.sum_range(10,20))

#Test fibonacci sequence
#print(bs.fib(1,1,6))
#print(bs.fib(1,1,10))
#print(bs.fib(1,1,100))

#Test faster fib
#print(bs.fast_fib(1,1,6))
#print(bs.fast_fib(1,1,10))
#print(bs.fast_fib(1,1,100))

#Test cartesian product function
#print(bs.cart_product({1,2}, {'a','b'}, {'x','y'})) #should be (1,a,x), (1,a,y), (1,b,x), (1,b,y)

#Test kcomb function
#print(bs.kcomb([1,2,3,4], 2))
#print(bs.kcomb([1,2,3,4,5,6], 3))

#sqrt((x*x/2.3 + 3.91304347826087))
#Tests the pipe function
#f1 = lambda x: x+3
#f2 = lambda x: x*x
#f3 = lambda x: x/2.3
#f4 = lambda x: x**.5
#my_pipe = bs.pipe([f1,f2,f3,f4])
#print(map(my_pipe, range(1,20)))