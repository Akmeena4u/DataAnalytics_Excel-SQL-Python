
## String Length, Slicing, and Looping in Python

Strings in Python are powerful for storing and manipulating textual data. Here's a breakdown of essential concepts:

**1. String Length:**

The `len()` function determines the number of characters in a string.

```python
fruit = "Mango"
length = len(fruit)
print("Mango is a", length, "letter word.")  # Output: Mango is a 5-letter word.
```

**2. String Slicing:**

Slicing extracts a portion of a string based on specified indices. Indices start from 0 (inclusive) and go up to the string length minus 1 (exclusive).

- **Slicing from Start:** Use `[:]` or specify the end index (not included).

```python
pie = "ApplePie"
print(pie[:5])  # Output: Apple (from index 0 to 4)
```

- **Slicing till End:** Use `[start:]` or omit the end index.

```python
print(pie[5:])  # Output: Pie (from index 5 to the end)
```

- **Slicing in Between:** Specify both start and end indices.

```python
print(pie[2:6])  # Output: pleP (from index 2 to 5)
```

- **Slicing Using Negative Indices:** Start from the end. -1 refers to the last character, -2 to the second-last, and so on.

```python
print(pie[-8:])  # Output: ApplePie (from index -8 to the end, same as pie[:])
```

**3. Looping Through Strings:**

Strings are iterable, meaning you can use `for` loops to process each character individually:

```python
alphabets = "ABCDE"
for char in alphabets:
    print(char)  # Output: A, B, C, D, E (each character on a new line)
```

**Additional Notes:**

- Slicing creates a new string, leaving the original string unmodified.
- You can use steps in slicing to extract characters at specific intervals (e.g., `string[::2]` for every other character).
- String methods like `upper()` and `lower()` can be used to convert case.

By understanding these techniques, you can effectively work with strings in your Python programs, extracting substrings, iterating over characters, and performing various text manipulations.
