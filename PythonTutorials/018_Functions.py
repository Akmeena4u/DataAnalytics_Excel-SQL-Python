"""Functions :- A function is a block of code that performs a specific task whenever it is called. 
There are two types of functions:

Built-in functions: These functions are defined and pre-coded in python.  Example :- min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

User-defined functions: We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

Syntax:
def function_name(parameters):
  pass
  # Code and Statements
  
Calling a function: We call a function by giving the function name, followed by parameters (if any) in the parenthesis.
 """

def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
#Output: Hello, Sam Wilson





def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

#if u wants to write function body later then use pass keyword in body so that code do not give error
def isLesser(a, b):
  pass        
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)     in absence of function we needs to do same each time  for all val of a and b
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
