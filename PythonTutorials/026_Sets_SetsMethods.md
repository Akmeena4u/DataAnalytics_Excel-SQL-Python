## Sets in Python: Unordered Collections of Unique Elements

Sets are fundamental data structures in Python that store collections of unique items. Unlike lists, the order of elements in a set is irrelevant, and duplicate values are not allowed.

**Key Points:**

- Enclosed in curly braces `{}`.
- Can contain elements of various data types.
- Unordered: elements do not have a specific order.
- Unchangeable: elements cannot be modified after creation (use lists if mutability is needed).
- Duplicates are not allowed.

**Example:**

```python
# Set of mixed data types
info = {"Carla", 19, False, 5.9}
print(info)  # Output: {False, 19, 5.9, 'Carla'} (order may vary)
```

**Accessing Set Items:**

- Sets don't support indexing due to their unordered nature.
- Use a `for` loop to iterate through elements.

```python
for item in info:
    print(item)
```

**Set Operations:**

- Sets support various operations similar to mathematical sets.

**1. Union and Intersection:**

  - `union()` and `update()`: Combine elements from both sets.
    - `union()` returns a new set with all unique elements.
    - `update()` modifies the original set by adding elements from the other set.

  - `intersection()` and `intersection_update()`: Find common elements in both sets.
    - `intersection()` returns a new set with elements present in both sets.
    - `intersection_update()` modifies the original set by keeping only common elements.

  - `symmetric_difference()` and `symmetric_difference_update()`: Find elements that are unique to either set.
    - `symmetric_difference()` returns a new set with elements not present in both sets.
    - `symmetric_difference_update()` modifies the original set by keeping only elements unique to it.

  - `difference()` and `difference_update()`: Find elements present only in the original set.
    - `difference()` returns a new set with elements from the original set that are not in the other set.
    - `difference_update()` modifies the original set by removing elements present in the other set.

**Example:**

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# Union with new set
cities3 = cities.union(cities2)
print(cities3)  # Output: {'Seoul', 'Kabul', 'Tokyo', 'Madrid', 'Berlin', 'Delhi'}

# Intersection with new set
cities4 = cities.intersection(cities2)
print(cities4)  # Output: {'Tokyo', 'Madrid'}
```

**2. Checking Set Relationships:**

  - `isdisjoint()`: Returns `True` if sets have no common elements.
  - `issuperset()`: Returns `True` if all elements of one set are in the other.
  - `issubset()`: Returns `True` if all elements of one set are in the other (but not necessarily the same set).

**Example:**

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
cities3 = {"Delhi", "Madrid"}

print(cities.isdisjoint(cities2))  # Output: False (common elements exist)
print(cities.issuperset(cities3))  # Output: True (all elements of cities3 are in cities)
print(cities2.issubset(cities))  # Output: False (not all elements of cities2 are in cities)
```

**Set Methods:**

- Python provides built-in methods for set manipulation:

  - `add(item)`: Adds a single element to the set.
  - `update(iterable)`: Adds multiple elements from an iterable (list, tuple, set, etc.) to the set.
  - `remove(item)`: Removes a specified element (raises an error if not found).
  - `discard(item)`: Removes a specified element (silently ignores if not found).
  - `pop()`: Removes and returns an arbitrary element (sets are unordered).
  - `clear()`: Removes all elements from the set.

**Example:**

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

cities.add("Helsinki")
print(cities)  # Output: {'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}

cities.update({"Warsaw", "Seoul"})
print(cities)  # Output: {'Seoul
