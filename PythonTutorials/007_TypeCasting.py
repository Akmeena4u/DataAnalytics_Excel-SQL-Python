""" Typecasting in Python:-The conversion of one data type into another data type is known as type casting in Python or type conversion in Python.

Two Types of Typecasting:
1-Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.
It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .  """

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
#Output: The Sum of both the numbers is 22


#--------------------------------------------------------------------------------------------------------------------------------


"""2-Implicit type casting:
Data types in Python do not have the same level .  According to the level, one data type is converted into another by the Python interpreter itself (automatically).
Python converts a smaller data type to a higher data type to prevent data loss."""

a = 7
print(type(a))
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

""" Ouput:
10.0
<class 'float'> """
