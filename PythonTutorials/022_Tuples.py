"""Python Tuples : Tuples are ordered collections of data items. They store multiple items in a single variable.
Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation."""

tuple = (1,2,2,3,5,4,6)
print(tuple)               #Output: (1, 2, 2, 3, 5, 4, 6)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)              #Output: ('Abhijeet', 18, 'FYBScIT', 9.8)



#Tuple Indexes Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0] and so on.
#Important Note :--All operations will be remain same as we have seen in lists like accessing tuple items , indexing , in keyword , and slicing etc...


#---------------------------------------------------------------------------------------------------------------------------------------

Manipulating Tuples: Tuples are immutable, hence if you want to add, remove, or change tuple items, then first you must convert the tuple to a list.
Then perform an operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)           #Output: ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')

#Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

#However, we can directly concatenate two tuples without converting them to list.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)       #Output: ('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')





#-------------------------------------Tuple methods----------------------------------------------------------------------------------

Tuple methods : As tuple is immutable type of collection of elements it have limited built in methods.

#1-count() Method : The count() method of Tuple returns the number of times the given element appears in the tuple.
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)         #Output 3


#2-index() method The Index() method returns the first occurrence of the given element from the tuple.
#Note: This method raises a ValueError if the element is not found in the tuple.
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)       #Output 3



#Important Note:-- If u wants to access all lists methods then u should convert it in list and then manipulate and then again convert to tuple
