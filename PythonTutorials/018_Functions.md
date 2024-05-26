## Functions in Python: Built-in and User-Defined

Functions are fundamental building blocks in Python. They allow you to create reusable blocks of code that perform specific tasks. This promotes code organization, modularity, and maintainability.

**Types of Functions:**

1. **Built-in Functions:**
   - Predefined functions available within the Python interpreter.
   - Examples: `print()`, `min()`, `max()`, `len()`, `sum()`, `type()`, `range()`, etc.
   - You can directly use them in your code without defining them explicitly.

2. **User-Defined Functions:**
   - You create these functions to encapsulate specific tasks.
   - They offer flexibility and customization for your programming needs.

**Syntax:**

```python
def function_name(parameters):
    """ (Optional Docstring) """  # Description of the function's purpose
    # Code and statements to be executed
```

- `def`: Keyword that declares the start of a function definition.
- `function_name`: A descriptive name for your function (follows variable naming conventions).
- `parameters`: Optional comma-separated list of arguments the function can receive.
  - Parameters allow you to provide input values to the function.
- `Docstring` (Optional): A brief explanation of the function's purpose and behavior.
  - Docstrings improve code readability and maintainability.
- `# Code and statements`: The code block that defines the function's behavior.

**Calling a Function:**

- Use the function name followed by parentheses.
- If the function takes parameters, provide the values within the parentheses, separated by commas.

**Example:**

```python
def greet(first_name, last_name):
    """Prints a greeting message."""
    print("Hello,", first_name, last_name)

greet("Alice", "Bob")  # Output: Hello, Alice Bob

def geometric_mean(a, b):
    """Calculates the geometric mean of two numbers."""
    product = a * b
    mean = product / (a + b)
    print(mean)

def compare_numbers(a, b):
    """Compares two numbers and prints a message."""
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or equal")

a = 9
b = 8

compare_numbers(a, b)  # Output: First number is greater
geometric_mean(a, b)  # Output: calculated geometric mean

c = 8
d = 74

compare_numbers(c, d)  # Output: Second number is greater or equal
geometric_mean(c, d)  # Output: calculated geometric mean
```

**Advantages of Functions:**

- **Code Reusability:**
   - Functions allow you to avoid redundant code by defining a task once and calling it multiple times with different inputs.
- **Improved Organization:**
   - Functions help break down your code into smaller, more manageable modules.
- **Enhanced Readability:**
   - Descriptive function names and docstrings make your code easier to understand.
- **Modular Testing:**
   - You can test individual functions separately, making debugging and maintenance simpler.

By effectively using built-in and user-defined functions, you can create well-structured, efficient, and maintainable Python programs.
