## String Formatting in Python: Old vs. New Methods

String formatting allows you to create dynamic strings by inserting values or expressions within them. Python offers two main approaches:

**1. Old Method: `str.format()`**

- Predefined method on string objects.
- Placeholders `{}` mark insertion points for values.
- Values are provided as keyword arguments or within a positional argument tuple.

**Example:**

```python
txt = "For only ${price:.2f} dollars!"
price = 49
print(txt.format(price=price))  # Output: For only $49.00 dollars!
```

**2. New Method: f-Strings (Introduced in Python 3.6)**

- More concise and readable syntax.
- Prefix the string literal with `f` or `F`.
- Embed expressions directly within curly braces `{}`.

**Example:**

```python
val = "Geeks"
print(f"{val}for{val} is a portal for {val}.")  # Output: GeeksforGeeks is a portal for Geeks

name = "Tushar"
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")  # Output: Hello, My name is Tushar and I'm 23 years old.
```

**Advantages of f-Strings:**

- Simpler and more readable syntax compared to `str.format()`.
- Can perform arbitrary expressions within curly braces.
- Supports multi-line strings using triple quotes (`"""` or `'''`).

**Example (Multi-line f-String):**

```python
user = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

message = f"""
Hello, {user['name']}!

You are {user['age']} years old and live in {user['city']}.
"""

print(message)
```

**Choosing the Right Method:**

- For Python versions before 3.6, or for more complex formatting requirements, `str.format()` might be more suitable.
- For Python 3.6 and later, f-strings are generally preferred due to their readability and ease of use.
