## Static Methods in Python

Static methods are a type of method in Python that belong to a class rather than an instance of the class. They are defined using the `@staticmethod` decorator and have several key characteristics:

* **No access to self:** Static methods cannot access the instance of the class (i.e., `self`). This means they cannot modify instance attributes.
* **Called on the class:** Static methods are called on the class itself, not on an instance.
* **Utility functions:** They are often used to create utility functions that don't need access to instance data or functionality specific to a particular object.

**Example:**

```python
class Math:
  @staticmethod
  def add(a, b):
    return a + b

result = Math.add(1, 2)
print(result)  # Output: 3
```

In this example, the `add` method is a static method of the `Math` class. It takes two arguments (`a` and `b`) and returns their sum. Notice that the method is called directly on the class (`Math.add`) without creating an instance.

**Key Points:**

* Static methods are useful for creating helper functions that are related to the class but don't require instance-specific data.
* They promote code reusability by encapsulating common functionality within the class.

**Additional Notes:**

The provided example also demonstrates a regular instance method (`addtonum`) that modifies the `num` attribute of an instance. This highlights the difference between static and instance methods.

---

## Class Methods in Python

In Python, class methods are a special type of method within a class that operate on the class itself rather than on an instance of the class. They are defined using the `@classmethod` decorator.

### Key Points

* **Bound to the class:** Class methods are associated with the class and not specific instances.
* **`cls` argument:** The first argument of a class method is always `cls`, which represents the class itself.
* **Use cases:**
    * Factory methods: Creating instances of the class in a specific way.
    * Alternative constructors: Providing multiple ways to initialize objects.
    * Utility functions: Functions that operate on the class itself (e.g., modifying a class variable).

### Example

```python
class Employee:
  company = "Apple"  # Class variable

  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany  # Modifying class variable

e1 = Employee()
e1.name = "Harry"
e1.show()  # Output: The name is Harry and company is Apple

e1.changeCompany("Tesla")  # Calling class method to change company

e1.show()  # Output: The name is Harry and company is Tesla
print(Employee.company)  # Output: Tesla (company variable updated)
```

### Conclusion

Class methods offer a way to define functions that work with the class itself or its attributes. They promote code reusability and flexibility in object creation and class manipulation.

---
## Super Keyword

The `super` keyword in Python is used to access methods and attributes of a parent (or superclass) from a child (or subclass) class. It's a powerful tool for working with inheritance hierarchies.

Here's a breakdown of how `super` works:

**Functionality:**

* **Calling parent class methods:** When you call a method in a child class that also exists in the parent class, you might want to call the parent class's implementation as well. `super` allows you to do this explicitly.
* **Accessing parent class attributes:** Similarly, you can use `super` to access attributes defined in the parent class.

**Syntax:**

There are two main ways to use `super`:

1. **With one argument:**

   ```python
   super(ChildClass, self).method_name(arguments)
   ```

   - `ChildClass`: This represents the child class where you're using `super`.
   - `self`: This refers to the current object instance of the child class.
   - `method_name`: The name of the method you want to call from the parent class.
   - `arguments`: Any arguments you want to pass to the parent class method.

2. **Without arguments (less common):**

   ```python
   super().method_name(arguments)
   ```

   - This assumes you're already inside a method of the child class and `self` is implicitly available.

**Example:**

```python
class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    super().make_sound()  # Call parent class method
    print("Woof!")

animal = Animal()
animal.make_sound()  # Output: Generic animal sound

dog = Dog()
dog.make_sound()      # Output: Generic animal sound
                       #         Woof!
```

In this example, the `Dog` class inherits from the `Animal` class. The `make_sound` method in the `Dog` class first calls the parent class's `make_sound` method using `super` to maintain the generic animal sound, and then adds the specific dog sound "Woof!".

**Key Points:**

* `super` helps you avoid code duplication by calling methods from the parent class.
* It ensures proper method resolution order (MRO) when dealing with multiple inheritance.
* Using `super` is generally considered good practice for clean and maintainable inheritance hierarchies.
---
