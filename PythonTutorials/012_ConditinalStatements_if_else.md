## Conditional Statements in Python: if, elif, and Nested if-else

Conditional statements allow your Python programs to make decisions based on certain conditions. Here's a breakdown of the primary conditional statements:

**1. if-else Statements:**

- The `if` statement evaluates a condition. If the condition is `True`, the code block within the `if` statement executes.
- The optional `else` statement provides an alternative code block to execute if the condition in the `if` statement is `False`.

**Example:**

```python
apple_price = 210
budget = 200

if apple_price <= budget:
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```

**Output:**

```
Alexa, do not add Apples to the cart.
```

**2. elif Statements (Multiple Conditions):**

- The `elif` statement (else if) allows you to check more than one condition. It executes if the condition in the `if` statement is `False` and the condition in the `elif` statement is `True`.
- You can have multiple `elif` statements chained together.

**Example:**

```python
number = 0

if number < 0:
    print("Number is negative.")
elif number == 0:
    print("Number is Zero.")
else:
    print("Number is positive.")
```

**Output:**

```
Number is Zero.
```

**3. Nested if-else Statements:**

- You can use `if`, `elif`, and `else` statements within other conditional statements to create complex decision logic.

**Example:**

```python
number = 18

if number < 0:
    print("Number is negative.")
elif number > 0:
    if number <= 10:
        print("Number is between 1-10")
    elif number > 10 and number <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
```

**Output:**

```
Number is between 11-20
```

By understanding and using these conditional statements effectively, you can control the flow of your Python programs, making them more flexible and responsive to different conditions.
