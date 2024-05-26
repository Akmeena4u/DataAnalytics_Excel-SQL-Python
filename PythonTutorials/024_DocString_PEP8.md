## Docstrings in Python: Essential Documentation for Code

Docstrings are a crucial component of well-written Python code. They provide clear and concise explanations of functions, methods, classes, and modules, enhancing code readability and maintainability.

**Key Points:**

- Docstrings are string literals placed right after the definition of a Python object (function, method, class, module).
- Not executed by the Python interpreter but serve as documentation for human understanding.
- Accessed using the `__doc__` attribute of the object.

**Example:**

```python
def square(n):
    """Calculates and returns the square of a number."""
    return n**2

print(square(5))  # Output: 25
print(square.__doc__)  # Output: Calculates and returns the square of a number.
```

**Benefits of Docstrings:**

- Improve code clarity and understanding for others (and future you!).
- Enhance code maintainability by documenting purpose, behavior, and usage.
- Enable tools like `help()` or IDE features to automatically display docstrings.

**Docstring Styles:**

- **Short Description Docstrings:** Briefly summarize the object's purpose (one line).

```python
def greet(name):
    """Greets someone by name."""
    print(f"Hello, {name}!")
```

- **PEP 257 Docstrings:** More detailed format with explanations, parameters, return values, and examples.

```python
def factorial(n):
    """Calculates and returns the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(-2)
        ValueError: n must be non-negative
    """

    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

**Choosing a Docstring Style:**

- The level of detail depends on the complexity of the object and your project's requirements.
- For simpler functions, a short description might suffice.
- For complex functions, classes, or modules, consider PEP 257 style for comprehensive documentation.

**Remember:** Consistent use of docstrings across your codebase promotes better code quality and collaboration. By effectively utilizing docstrings, you can dramatically improve the readability and maintainability of your Python programs.
