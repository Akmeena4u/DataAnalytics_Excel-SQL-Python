## Function Arguments and Return Statements in Python

Functions in Python offer flexibility in how you provide input (arguments) and retrieve output (return values). Here's a breakdown of the different types of arguments and return statements:

**Function Arguments:**

- Arguments are values you pass to a function when you call it.
- They allow you to customize the function's behavior for different scenarios.

**Types of Arguments:**

1. **Default Arguments:**
   - You can assign default values to function parameters during definition.
   - If you don't provide an argument when calling the function, the default value is used.

**Example:**

```python
def greet(first_name, middle_name="Jhon", last_name="Doe"):
    """Greets someone by name."""
    print("Hello,", first_name, middle_name, last_name)

greet("Alice")  # Output: Hello, Alice Jhon Doe
```

2. **Keyword Arguments:**
   - Arguments are passed with `key=value` pairs in the function call.
   - The order of arguments becomes irrelevant; they are matched by name.

**Example:**

```python
def greet(first_name, middle_name, last_name):
    """Greets someone by name."""
    print("Hello,", first_name, middle_name, last_name)

greet(last_name="Smith", first_name="Bob", middle_name="M.")  # Output: Hello, Bob M. Smith
```

3. **Required Arguments:**
   - These are arguments that must be provided when calling the function.
   - If required arguments are missing, a `TypeError` occurs.

**Example:**

```python
def greet(first_name, middle_name, last_name):
    """Greets someone by name."""
    print("Hello,", first_name, middle_name, last_name)

# greet("Alice", "Bob")  # TypeError: missing required argument: 'last_name'
greet("Alice", "Bob", "Jones")  # Output: Hello, Alice Bob Jones
```

4. **Variable-Length Arguments:**

   - **Arbitrary Arguments (`*args`):**
     - Capture a variable number of positional arguments as a tuple.
     - Use `*args` in the function definition to access them.

   - **Keyword Arbitrary Arguments (`**kwargs`):**
     - Capture a variable number of keyword arguments as a dictionary.
     - Use `**kwargs` in the function definition to access them.

**Example:**

```python
# Arbitrary arguments
def greet_all(*names):
    """Greets multiple people."""
    for name in names:
        print(f"Hello, {name}")

greet_all("Alice", "Bob", "Charlie")  # Output: Hello, Alice; Hello, Bob; Hello, Charlie

# Keyword arbitrary arguments
def greet_with_details(fname, lname, **info):
    """Greets someone with optional details."""
    print(f"Hello, {fname} {lname}")
    for key, value in info.items():
        print(f"{key}: {value}")

greet_with_details(fname="Alice", lname="Smith", age=30, city="New York")
# Output: Hello, Alice Smith; age: 30; city: New York
```

**Return Statements:**

- The `return` statement within a function specifies a value to send back to the calling code.
- The function execution stops after the `return` statement.

**Example:**

```python
def calculate_area(length, width):
    """Calculates and returns the area of a rectangle."""
    area = length * width
    return area

result = calculate_area(5, 4)  # result will be 20
print(f"The area is: {result}")  # Output: The area is: 20
```

By understanding and using arguments and return statements effectively, you can create well-structured, flexible, and reusable functions in Python.
