**Else Block with Loops in Python**

Python's `for` and `while` loops can optionally include an `else` block. This block executes only after the entire loop finishes iterating, under the following conditions:

- **`for` loop:** The `else` block executes if the loop completes without encountering a `break` statement.
- **`while` loop:** The `else` block executes if the loop condition eventually becomes `False` and the loop terminates normally.

**Example (for loop):**

```python
for x in range(5):
    print("iteration no {} in for loop".format(x + 1))
else:
    print("else block in loop")
print("Out of loop")
```

**Output:**

```
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop
```

**Key Points:**

- The `else` block is a useful way to execute code that should only run after the loop's normal completion.
- If a `break` statement is encountered within the loop, the `else` block is skipped.

**Example (while loop with else):**

```python
x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("else block in loop")
print("Out of loop")
```

**Output:**

```
0
1
2
3
4
else block in loop
Out of loop
```

**In summary, the `else` block with loops provides a way to conditionally execute code after a loop's regular iteration, enhancing code readability and structure.**
