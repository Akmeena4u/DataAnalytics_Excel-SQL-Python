# Taking User Input in Python
# In Python, we can take user input directly by using the input() function. This input function gives a return value as a string/character hence we have to pass that into a variable


variable=input()
#But the input function returns the value as a string. Hence we have to typecast them whenever required to another datatype.
variable=int(input())
variable=float(input())

#We can also display a text using the input function. This will make the input() function take user input and display a message as well


a=input("Enter the name: ")   #here this will wait until u type any val
print(a)
