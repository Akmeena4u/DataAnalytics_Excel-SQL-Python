#List Methods
#1- list.sort() : This method sorts the list in ascending order. The original list is updated
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)                     #output : ['blue', 'green', 'indigo', 'voilet']

#What if you want to print the list in descending order? -- We must give reverse=True as a parameter in the sort method.The reverse parameter is set to False by default.
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)                   #output : ['voilet', 'indigo', 'green', 'blue']



#2-reverse() -- This method reverses the order of the list.
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)                  #output : ['green', 'blue', 'indigo', 'voilet']



#3-index() : This method returns the index of the first occurrence of the list item.
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))    #output : 1



#4 -count() : Returns the count of the number of items with the given value.
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))   #Output:2


#5-copy() : Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)                 #Output: ['voilet', 'green', 'indigo', 'blue']
print(newlist)                # Output: ['voilet', 'green', 'indigo', 'blue']


#6-append(): This method appends items to the end of the existing list.
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)                #Output:['voilet', 'indigo', 'blue', 'green']


#7-insert():This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
colors = ["voilet", "indigo", "blue"]
colors.insert(1, "green")   #inserts item at index 1
print(colors)                #Output: ['voilet', 'green', 'indigo', 'blue']



#8-extend():This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)               #Output:['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

#Concatenating two lists: You can simply concatenate two lists to join two lists.
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)     #Output: ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
