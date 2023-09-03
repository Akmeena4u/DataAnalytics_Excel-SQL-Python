#while Loop : As the name suggests,  while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

count = 5
while (count > 0):
  print(count)                         #Output: 5 4 3 2 1  in new lines 
  count = count - 1
  
#Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.



"""Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed."""

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
#output:   5 4 3 2 1  in new lines   and in next line --  counter is 0
