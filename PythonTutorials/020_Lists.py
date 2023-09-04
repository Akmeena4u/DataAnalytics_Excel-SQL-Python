
"""Lists are ordered collection of data items.They store multiple items in a single variable.List items are separated by commas and enclosed within square brackets [].
Lists are changeable meaning we can alter them after creation.a single list can contain items of different data types."""


lst1 = [1,2,2,3,5,4,6]
print(lst1)                        #Output:[1, 2, 2, 3, 5, 4, 6]

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)                    #Output: ['Abhijeet', 18, 'FYBScIT', 9.8]





#--------------------------------------------------------------------------------------------------------------------------

#List Index :- Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1].

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

#Accessing list items :- We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

#Positive Indexing: As we have seen that list items have index, as such we can access items using these indexes.

print(colors[2])                     #output - Blue
print(colors[4])                     #output Green
  
#Negative Indexing: Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2]and so on.

Example:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])                  #output Green      simple before negative index add len(list)-negativeindex to access everthing from front
print(colors[-3])                  #output  Blue






#-------------------------------------------------------------------------------------------------------------------------------------------

#Check whether an item in present in the list? --We can check if a given item is present in the list. This is done using the in keyword.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
#Output: Yellow is present.





#---------------------------------------------------------------------------------------------------------------------------------------------------
#Range of Index: You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

#Syntax: listName[start : end : jumpIndex]  Note: jump Index is optional

#Example: printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes              Output: ['mouse', 'pig', 'horse', 'donkey']
print(animals[-7:-2])	#using negative indexes'            output : ['bat', 'mouse', 'pig', 'horse', 'donkey']

#Note: The element of the end index provided will not be included.  and list slicing will be same as we learn in string


#Example: Printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes              Output: ['cat', 'bat', 'pig', 'donkey', 'cow']
print(animals[-8:-1:2])	#using negative indexes            output : ['dog', 'mouse', 'horse', 'goat']




#----------------------------------List Comprehension----------------------------------------------------------------------------------------

List Comprehensionn : List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
Syntax:    List = [Expression(item) for item in iterable if Condition]         Expression: It is the item which is being iterated.


#Example : Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
#Output: ['Sarah', 'Bruno', 'Anastasia']
