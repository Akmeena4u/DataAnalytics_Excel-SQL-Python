
# Modules and pip in Python!

A module is like a code library which can be used to borrow code written by somebody else in our Python program. There are two types of modules in Python:

## Built-in Modules

These modules are ready to import and use and ship with the Python interpreter. There is no need to install such modules explicitly.

## External Modules

These modules are imported from a third-party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of the same module over time.

## The pip Command

It can be used as a package manager to install a Python module. Let's install a module called pandas using the following command:

```sh
pip install pandas
```

Similarly, we can install other modules and look into their documentation for usage instructions.

```python
import pandas  # This is an example of an external module
import hashlib  # This is an example of a built-in module

print("Hi")

# Don't worry about how to use these modules just yet!
pandas.read_csv("one.csv")
m = hashlib.sha256()
```
