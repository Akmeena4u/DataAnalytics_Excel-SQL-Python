"""if-else Statements :- Sometimes the programmer needs to check the evaluation of certain expression(s) based on some conditions and After execution return to the code out of the if……else block.
Based on this, the conditional statements are further classified into following types: if , if-else , if-else-elif ,nested if-else-elif."""

#1-if-else example
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
#Output: Alexa, do not add Apples to the cart.



#2-elif Statements Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")
#Output: Number is Zero.


#3-Nested if statements  :-  We can use if, if-else, elif statements inside other if statements as well.
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
#Output: Number is between 11-20
