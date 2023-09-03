# Variables 
# What is a variable? --Variable is like a container that holds data

a = 1
b = True
c = "Harry"
d = None
# These are four variables of different data types.

#---------------------------------------------------------------------------------------------------------------

# What is a Data Type? --Data type specifies the type of value a variable holds.
# In Python, we can print the type of any operator using the type function:

a = 1
print(type(a))
b = "1"
print(type(b))

#By default, Python provides the following built-in data types:

#1. Numeric data: int, float, complex
#2. Text data: str
#3. Boolean data: Boolean data consists of values True or False.
#4. Sequenced data: list, tuple
    #list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.


    list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
    print(list1)
    #Output: [8, 2.3, [-4, 5], ['apple', 'banana']]

    #Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.


    tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
    print(tuple1)
    #Output: (('parrot', 'sparrow'), ('Lion', 'Tiger'))

#5. Mapped data: dict
     #dict: A dictionary is an unordered collection of data containing a key: value pair. The key: value pairs are enclosed within curly brackets.

    dict1 = {"name": "Sakshi", "age":20, "canVote": True}
    print(dict1)
    #Output: {'name': 'Sakshi', 'age': 20, 'canVote': True}
