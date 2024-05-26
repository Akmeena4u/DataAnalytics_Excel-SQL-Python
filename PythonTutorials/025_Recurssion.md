## Recursion in python : Recursion is the process of defining something in terms of itself.
```python
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code
num = 7; 
print("Factorial: ",factorial(num))
#Output: Factorial:  5040
```
