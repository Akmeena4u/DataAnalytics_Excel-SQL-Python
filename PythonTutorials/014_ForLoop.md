## Loops in Python: for and while

Loops are a fundamental concept in programming, allowing you to execute a block of code repeatedly until a specific condition is met. Python offers two primary loop types: `for` and `while`.

**1. for Loops:**

- `for` loops iterate over a sequence of items in an iterable object (like strings, lists, tuples, sets, dictionaries).
- In each iteration, the loop assigns the current item to a designated variable (usually `i` or a more descriptive name).
- The indented code block within the loop executes for each item in the sequence.

**Examples:**

```python
# Iterating over a string
name = 'Abhishek'
for letter in name:
    print(letter, end=", ")  # Output: A, b, h, i, s, h, e, k,

# Iterating over a list
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
```

**2. range() Function:**

- The `range()` function generates a sequence of numbers within a specified range.
- It takes up to three arguments: starting value (defaults to 0), ending value (not included), and step size (defaults to 1).

**Examples:**

```python
# Looping a specific number of times (0 to 4, excluding 5)
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4

# Looping from 4 to 8 (including 8)
for i in range(4, 9):
    print(i)  # Output: 4 5 6 7 8

# Looping with a step size of 2 (4, 6, and 8)
for i in range(4, 9, 2):
    print(i)  # Output: 4 6 8
```

**Key Differences:**

- `for` loops naturally iterate over items in a sequence.
- `range()` generates a sequence of numbers for the `for` loop to iterate over.

By effectively using `for` loops and the `range()` function, you can automate repetitive tasks and control the flow of your Python programs efficiently.
