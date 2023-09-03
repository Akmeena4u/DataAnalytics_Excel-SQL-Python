#its is new concept in python and it comes in python 3.10 and above versions only

"""Match Case Statements To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python.
A match statement will compare a given variable’s value to different shapes or cases , also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

Syntax:
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n

Note: unlike other languages here we do not need to use break statements in each case            
"""

x = int(input("Enter the value of x: "))   #lets asssume x=100    output=== 100 default case executed
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")
    #Note: Here inside cases or patterns we can also use if else statemnts
    case _ if x!=90:                  
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
     # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:  
    case _:
        print(x)


