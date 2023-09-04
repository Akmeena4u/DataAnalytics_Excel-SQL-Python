

"""This Python program uses the current time to greet the user with "Good Morning," "Good Afternoon," or "Good Night" based
on the time of day (morning, afternoon, or night) by determining the hour and displaying the appropriate greeting message."""

import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")
