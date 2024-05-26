## Dictionaries in Python: Key-Value Pair Collections

Dictionaries are fundamental data structures in Python that store collections of data items as key-value pairs. Unlike lists, dictionaries provide a flexible way to organize data using unique keys to access associated values.

**Key Points:**

- Enclosed in curly braces `{}`.
- Key-value pairs separated by colons `:`.
- Keys must be unique and immutable (e.g., strings, numbers, tuples).
- Values can be of any data type.
- Order of elements is maintained (as inserted).

**Example:**

```python
# Dictionary of personal information
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)  # Output: {'name': 'Karan', 'age': 19, 'eligible': True}
```

**Accessing Dictionary Items:**

- Use keys to access specific values.

**1. Single Value Access:**

  - Square brackets `[]`: `info['name']` retrieves the value associated with the key 'name'.
  - `get()` method: `info.get('eligible')` retrieves the value, returning `None` if the key doesn't exist.

**2. Multiple Value Access:**

  - `values()`: Returns a view of all values in the dictionary as a dictionary view object.
  - `keys()`: Returns a view of all keys in the dictionary as a dictionary view object.
  - `items()`: Returns a view of all key-value pairs in the dictionary as a dictionary items view object.

**Example:**

```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}

print(info.values())  # Output: dict_values(['Karan', 19, True])
print(info.keys())    # Output: dict_keys(['name', 'age', 'eligible'])
print(info.items())   # Output: dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
```

**Dictionary Methods:**

- Python provides built-in methods for manipulating dictionaries:

**1. Update:**

  - `update(iterable)`: Updates existing key-value pairs or adds new ones from an iterable (dictionary, list of key-value pairs).

**Example:**

```python
info = {'name': 'Karan', 'age': 19}
info.update({'age': 20, 'DOB': 2001})
print(info)  # Output: {'name': 'Karan', 'age': 20, 'DOB': 2001}
```

**2. Removing Items:**

  - `clear()`: Removes all key-value pairs from the dictionary.
  - `pop(key)`: Removes the key-value pair with the specified key and returns the value. Raises `KeyError` if the key is not found.
  - `popitem()`: Removes and returns an arbitrary key-value pair (useful when the specific key to remove is unknown).
  - `del keyword`: Removes a key-value pair with the specified key (similar to `pop()` but without returning the value). If used without a key, it deletes the entire dictionary.

**Example:**

```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}

info.clear()
print(info)  # Output: {}

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')
print(info)  # Output: {'name': 'Karan', 'age': 19}

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.popitem()
print(info)  # Output: {'name': 'Karan', 'age': 19} (or other possible output)

info = {'name': 'Karan', 'age': 19}
del info['age']
print(info)  # Output: {'name': 'Karan'}

info = {'name': 'Karan', 'age': 19}
del info
print(info)  # Output: NameError: name 'info' is not defined
```
