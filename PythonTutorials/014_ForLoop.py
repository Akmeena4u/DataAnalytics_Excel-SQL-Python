
""" Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;
for loop
while loop"""



#The for Loop - for loops can iterate over a sequence of iterable objects in Python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
#Example: iterating over a string:
name = 'Abhishek'
for i in name:
    print(i, end=", ")                       #Output:  A, b, h, i, s, h, e, k,

#Example: iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
#Similarly, we can use loops for lists, sets, and dictionaries.




#range(): What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?
for k in range(5):
    print(k , end=" ")                   #Output: 0 1 2 3 4
#Here, we can see that the loop starts from 0 by default and increments at each iteration.

#But we can also loop over a specific range.
for k in range(4,9):
    print(k)                             #Output: output will be 4 5 6 7 8 in different lines

for k in range(4,9,2)                #Note  this will print as above loop but each time it will take jump of 2  ----   output 4 6 8
    print(k)     
