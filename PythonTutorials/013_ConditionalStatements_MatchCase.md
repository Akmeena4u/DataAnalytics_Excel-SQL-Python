## Match-Case Statements in Python (Python 3.10+)

The match-case statement, introduced in Python 3.10, provides a powerful and concise way to implement switch-case-like functionality. It allows for pattern matching to compare a variable's value against different patterns and execute code blocks based on the matching pattern.

**Syntax:**

```python
match variable_name:
    case pattern1:
        # statement to execute if pattern1 matches
    case pattern2:
        # statement to execute if pattern2 matches
    ...
    case _:  # Default case (optional)
        # statement to execute if no other pattern matches
```

**Key Points:**

- Match statements compare a variable (`variable_name`) against various patterns.
- Patterns can be literals, ranges, or more complex expressions.
- Unlike `if-else` statements, `break` statements are not required within each case.
- The `_` wildcard pattern in a case matches any value (similar to the default case in `if-else`).
- Code within a matching case executes when the variable's value matches the pattern.
- The optional default case (`case _`) executes if no other pattern matches.

**Example:**

```python
x = int(input("Enter the value of x: "))  # Assume x = 100

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x != 90:  # Pattern matching with if-else within a case
        print(x, "is not 90")
    case _ if x != 80:
        print(x, "is not 80")
    case _:
        print(x)  # Default case (executed here for x = 100)
```

**Output:** (Assuming x = 100)

```
100
```

**Benefits of Match-Case Statements:**

- Readability: Match statements can improve code readability by making conditional logic more explicit and easier to follow.
- Expressiveness: They allow for pattern matching, making it easier to handle different value types and conditions within a single statement.
- Maintainability: With simpler conditional logic, code becomes easier to maintain and update.

By incorporating match-case statements into your Python code (starting from version 3.10), you can enhance code clarity, efficiency, and flexibility for handling various conditions and patterns.
