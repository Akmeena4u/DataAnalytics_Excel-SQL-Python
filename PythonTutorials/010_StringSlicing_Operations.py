
#Length of a String:- We can find the length of a string using the len() function.
  
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")    #Output: Mango is a 5-letter word.

String Slicing:--  method of specifying the start and end index to specify a part of a string is called slicing.

pie = "ApplePie"
print(pie[:5])      #Slicing from Start                        output:-  Apple
print(pie[5:])      #Slicing till End                          output:-  Pie
print(pie[2:6])     #Slicing in between                        output:-  pleP
print(pie[-8:])     #Slicing using negative index              output:-  ApplePie       Here at place of negative index python places--   len(pie)-8

#Loop through a String: Strings are arrays and arrays are iterable. Thus we can loop through strings.
  
alphabets = "ABCDE"
for i in alphabets:
    print(i)   # This will print each character line by line 
