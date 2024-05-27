## Access Specifiers/Modifiers in Python

Access specifiers or modifiers in Python programming are used to limit the access of class variables and methods outside of the class, supporting the concept of inheritance.

### Types of Access Specifiers

There are three main types of access specifiers in Python:

1. Public Access Modifier
2. Private Access Modifier (convention)
3. Protected Access Modifier (convention)

### Public Access Specifier

All variables and methods (member functions) in Python are public by default. Any instance variable in a class followed by the `self` keyword (e.g., `self.var_name`) is publicly accessible.

**Example:**

```python
class Student:
  def __init__(self, age, name):
    self.age = age  # public variable
    self.name = name  # public variable

obj = Student(21, "Harry")
print(obj.age)
print(obj.name)
```

**Output:**

```
21
Harry
```

### Private Access Modifier (convention)

In theory, Python does not have strict "private" access modifiers like some other programming languages. However, a convention is used to indicate that a variable or method should be considered private by prefixing its name with a double underscore (`__`). This is known as a "weak internal use indicator" and it's a convention, not a strict rule. Code outside the class can still access these "private" members, but it's generally understood that they should not be accessed or modified.

**Example:**

```python
class Student:
  def __init__(self, age, name):
    self.__age = age  # An indication of private variable

  def __funName(self):  # An indication of private function
    self.y = 34
    print(self.y)

class Subject(Student):
  pass

obj = Student(21, "Harry")
obj1 = Subject

# Calling by object of class Student
print(obj.__age)  # AttributeError
print(obj.__funName())  # AttributeError

# Calling by object of class Subject
print(obj1.__age)  # AttributeError
print(obj1.__funName())  # AttributeError
```

**Key points:**

* Private members cannot be accessed or inherited outside of the class.
* Trying to access or inherit private members in child classes results in an `AttributeError`.

**Name Mangling:**

Name mangling is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by adding a single leading underscore and a double leading underscore respectively.

**Example:**

```python
class MyClass:
  def __init__(self):
    self._nonmangled_attribute = "I am a nonmangled attribute"
    self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute)  # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute)  # Throws an AttributeError
print(my_object._MyClass__mangled_attribute)  # Output: I am a mangled attribute
```

In this example:

* `_nonmangled_attribute` is marked as nonmangled by convention, but can still be accessed from outside the class.
* `__mangled_attribute` is private and its name is mangled to `_MyClass__mangled_attribute`, so it cannot be accessed directly from outside the class. You can access it using `_MyClass__mangled_attribute`.


### Protected Access Modifier (convention)

In object-oriented programming (OOP), "protected" members (methods or attributes) are intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating a protected member is to prefix its name with a single underscore (`_`). For instance, if a class has a method named `_my_method`, it suggests that the method should only be accessed by the class itself and its subclasses.

**It's important to remember that the single underscore is just a naming convention and does not provide actual protection or restrict access to the member.**

**Example:**

```python
class Student:
  def __init__(self):
    self._name = "Harry"

  def _funName(self):  # protected method
    return "CodeWithHarry"

class Subject(Student):
  pass

obj = Student()
obj1 = Subject

# Calling by object of Student class
print(obj._name)
print(obj._funName())

# Calling by object of Subject class
print(obj1
```

---

## Inheritance in Python

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties and methods from another class. This enables code reusability and the creation of hierarchical relationships between classes.

### Inheritance Syntax

```python
class BaseClass:
  # Body of base class

class DerivedClass(BaseClass):
  # Body of derived class
```

The `DerivedClass` inherits features from the `BaseClass`. The derived class can add its own properties and methods as well.

### Types of Inheritance

There are five main types of inheritance in Python:

1. **Single Inheritance:** A derived class inherits from a single parent class. This is the most common type of inheritance and promotes code reusability.

**Example:**

```python
class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def bark(self):
    print("Woof!")

animal = Animal()
animal.make_sound()  # Generic animal sound

dog = Dog()
dog.make_sound()  # Generic animal sound
dog.bark()        # Woof!
```

2. **Multiple Inheritance:** A derived class inherits from multiple parent classes. This can be useful for combining functionalities from different classes, but it can also lead to complexity and ambiguity if the parent classes have methods with the same name.

**Example:**

```python
class Mother:
  def mother_info(self):
    print("Mother's information")

class Father:
  def father_info(self):
    print("Father's information")

class Child(Mother, Father):
  def child_info(self):
    print("Child's information")

child = Child()
child.mother_info()
child.father_info()
child.child_info()
```

3. **Multilevel Inheritance:** A derived class inherits from another derived class, which in turn inherits from a base class. This creates a chain of inheritance.

**Example:**

```python
class Grandparent:
  def grandparent_method(self):
    print("Grandparent method")

class Parent(Grandparent):
  def parent_method(self):
    print("Parent method")

class Child(Parent):
  def child_method(self):
    print("Child method")

child = Child()
child.grandparent_method()
child.parent_method()
child.child_method()
```

4. **Hierarchical Inheritance:** Multiple derived classes inherit from a single base class. This creates a hierarchy of classes with a common ancestor.

**Example:**

```python
class Vehicle:
  def move(self):
    print("The vehicle is moving")

class Car(Vehicle):
  def car_method(self):
    print("Car specific method")

class Bike(Vehicle):
  def bike_method(self):
    print("Bike specific method")

car = Car()
car.move()
car.car_method()

bike = Bike()
bike.move()
bike.bike_method()
```

5. **Hybrid Inheritance:** A combination of multiple inheritance types. This can be complex and is generally not recommended unless absolutely necessary.

**Note:** These are just basic examples to illustrate the concepts. Inheritance can become more complex in real-world applications.
