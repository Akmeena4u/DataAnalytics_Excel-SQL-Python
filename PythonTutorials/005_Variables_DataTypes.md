

### Variables

* A variable is a named container that holds data in your program.
* You can assign different types of values to variables.

**Example:**

```
a = 1  # Integer
b = True  # Boolean
c = "Harry"  # String
d = None  # None (special data type)
```

### Data Types

* Data types specify the kind of data a variable can hold.
* Python has built-in data types for different categories of data.

**Checking Data Types:**

```python
a = 1
print(type(a))  # Output: <class 'int'> (integer)

b = "1"
print(type(b))  # Output: <class 'str'> (string)
```

**Common Data Types:**

1. **Numeric:**
   - `int` (integer): Whole numbers (e.g., 10, -5)
   - `float` (floating-point): Numbers with decimals (e.g., 3.14, -2.5)
   - `complex` (complex): Numbers with a real and imaginary part (e.g., 3+2j)

2. **Text:**
   - `str` (string): Sequence of characters (e.g., "Hello", 'World!')

3. **Boolean:**
   - `bool`: Represents logical values `True` or `False`

4. **Sequenced:**
   - **List:** Ordered collection of items, changeable (uses square brackets `[]`)
   - **Tuple:** Ordered collection of items, unchangeable (uses parentheses `()`)

**Example of List:**

```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)  # Output: [8, 2.3, [-4, 5], ['apple', 'banana']]
```

**Example of Tuple:**

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)  # Output: (('parrot', 'sparrow'), ('Lion', 'Tiger'))
```

5. **Mapped:**
   - **Dictionary:** Collection of key-value pairs, unordered (uses curly braces `{}`)

**Example of Dictionary:**

```python
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)  # Output: {'name': 'Sakshi', 'age': 20, 'canVote': True}
```
