
Encapsulation and abstraction are two fundamental concepts in object-oriented programming (OOP) that help in designing and implementing robust and maintainable software.

### Encapsulation
Encapsulation is the mechanism of restricting access to certain details of an object and exposing only the necessary parts. This is achieved by bundling the data (attributes) and the methods (functions) that operate on the data into a single unit or class and controlling the access to the data through public methods.

#### Example of Encapsulation in Python:
```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

# Creating an object of the Employee class
emp = Employee("John", 50000)

# Accessing private attributes through public methods
print(emp.get_name())  # Output: John
emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000

# Trying to access private attributes directly (will raise an AttributeError)
# print(emp.__name)  # This will result in an error
```
In the above example:
- The `__name` and `__salary` attributes are private and cannot be accessed directly from outside the class.
- Public methods (`get_name`, `set_name`, `get_salary`, `set_salary`) are provided to access and modify the private attributes, thus encapsulating the internal state of the object.

### Abstraction
Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object. It simplifies the interface of a class and reduces complexity by providing a high-level view of the functionality.

#### Example of Abstraction in Python:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating objects of Rectangle and Circle classes
rect = Rectangle(10, 20)
circ = Circle(5)

print("Rectangle Area:", rect.area())  # Output: Rectangle Area: 200
print("Rectangle Perimeter:", rect.perimeter())  # Output: Rectangle Perimeter: 60
print("Circle Area:", circ.area())  # Output: Circle Area: 78.5
print("Circle Perimeter:", circ.perimeter())  # Output: Circle Perimeter: 31.400000000000002
```
In the above example:
- `Shape` is an abstract base class with abstract methods `area` and `perimeter`.
- `Rectangle` and `Circle` are concrete classes that inherit from `Shape` and implement the abstract methods.
- The details of how the area and perimeter are calculated are hidden from the users of these classes. They only interact with the high-level methods (`area` and `perimeter`), providing a clear and simple interface.

### Summary:
- **Encapsulation** bundles data and methods into a single unit and restricts direct access to some of the object's components, exposing only necessary methods.
- **Abstraction** hides the complex implementation details and shows only the essential features, simplifying the user interface of a class.

Both concepts work together to create a well-structured and easy-to-maintain codebase.
---

## Polymorphism

Polymorphism in Python is a concept that allows objects of different types to be treated as objects of a common super type. It is one of the core concepts of object-oriented programming (OOP) and can be used to perform a single action in different ways. There are two main types of polymorphism in Python:

1. **Duck Typing**: Python is dynamically typed, meaning that it focuses on whether an object can perform the required behavior (methods and properties), rather than the actual type of the object. This is often summarized by the phrase, "If it looks like a duck and quacks like a duck, it must be a duck." Here is an example:

    ```python
    class Dog:
        def speak(self):
            return "Woof!"

    class Cat:
        def speak(self):
            return "Meow!"

    class Cow:
        def speak(self):
            return "Moo!"

    def animal_sound(animal):
        print(animal.speak())

    dog = Dog()
    cat = Cat()
    cow = Cow()

    animal_sound(dog)  # Output: Woof!
    animal_sound(cat)  # Output: Meow!
    animal_sound(cow)  # Output: Moo!
    ```

2. **Method Overriding**: This involves redefining a method in a subclass that already exists in the parent class. This allows the subclass to provide a specific implementation of the method that is different from the parent class. Here is an example:

    ```python
    class Animal:
        def speak(self):
            return "Some sound"

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    def animal_sound(animal):
        print(animal.speak())

    dog = Dog()
    cat = Cat()

    animal_sound(dog)  # Output: Woof!
    animal_sound(cat)  # Output: Meow!
    ```
3. **Method Overloading**

Method overloading is the ability to define multiple methods with the same name but different parameters (either in type or number) within the same class. However, Python does not support method overloading in the traditional sense found in statically typed languages like Java or C++. In Python, the latest defined method with a given name will override any previous methods with the same name.

Instead, Python achieves similar functionality using default arguments or variable-length argument lists (`*args` and `**args`).

#### Example of Method Overloading using Default Arguments:
```python
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

math_op = MathOperations()
print(math_op.add(5, 3))      # Output: 8
print(math_op.add(5, 3, 2))   # Output: 10
```
In this example, the `add` method can be called with either two or three arguments. The third argument `c` is optional and defaults to 0 if not provided.

#### Example of Method Overloading using Variable-Length Arguments:
```python
class MathOperations:
    def add(self, *args):
        return sum(args)

math_op = MathOperations()
print(math_op.add(5, 3))           # Output: 8
print(math_op.add(5, 3, 2, 1))     # Output: 11
print(math_op.add(1, 2, 3, 4, 5))  # Output: 15
```
In this example, the `add` method can take any number of arguments due to the use of `*args`, making it flexible to handle different numbers of inputs.

4. **Operator Overloading**

Operator overloading allows you to define or change the behavior of operators (+, -, *, etc.) for user-defined classes. This is done by defining special methods in your class, which Python internally maps to the operators.

#### Example of Operator Overloading:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)

v3 = v1 + v2
v4 = v1 - v2

print(v3)  # Output: Vector(7, 10)
print(v4)  # Output: Vector(-3, -4)
```
In this example:
- The `__add__` method is defined to overload the `+` operator.
- The `__sub__` method is defined to overload the `-` operator.
- The `__str__` method is defined to provide a human-readable string representation of the `Vector` object.

### Key Points:
- **Method Overloading** in Python is achieved using default arguments or variable-length arguments, as Python does not support traditional method overloading.
- **Operator Overloading** allows you to define custom behavior for standard operators by implementing special methods in your class.

### Special Methods for Operator Overloading:
- `__add__(self, other)` for the `+` operator.
-
 `__sub__(self, other)` for the `-` operator.
- `__mul__(self, other)` for the `*` operator.
- `__truediv__(self, other)` for the `/` operator.
- `__floordiv__(self, other)` for the `//` operator.
- `__mod__(self, other)` for the `%` operator.
- `__pow__(self, other)` for the `**` operator.
- `__eq__(self, other)` for the `==` operator.
- `__ne__(self, other)` for the `!=` operator.
- `__lt__(self, other)` for the `<` operator.
- `__le__(self, other)` for the `<=` operator.
- `__gt__(self, other)` for the `>` operator.
- `__ge__(self, other)` for the `>=` operator.

By using these special methods, you can customize how operators work with your classes, enhancing the readability and functionality of your code.
### Benefits of Polymorphism

- **Code Reusability**: Polymorphism allows you to write more generic and reusable code.
- **Flexibility**: It makes it easier to add new classes and methods without changing existing code.
- **Maintainability**: Reduces code redundancy and simplifies the codebase, making it easier to maintain and extend.

### Practical Examples

- **Polymorphic Functions**: Functions that can take arguments of different types and handle them using common behavior.

    ```python
    def add(x, y):
        return x + y

    print(add(1, 2))           # Output: 3 (integer addition)
    print(add("Hello, ", "world!"))  # Output: Hello, world! (string concatenation)
    print(add([1, 2], [3, 4])) # Output: [1, 2, 3, 4] (list concatenation)
    ```

- **Polymorphic Classes**: Using polymorphism in class design to interact with objects of different types through a common interface.

    ```python
    class Shape:
        def area(self):
            pass

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius * self.radius

    shapes = [Rectangle(10, 20), Circle(5)]

    for shape in shapes:
        print(shape.area())
        # Output:
        # 200
        # 78.5
    ```

In summary, polymorphism is a powerful feature in Python that enhances the flexibility and maintainability of your code by allowing objects of different types to be treated through a common interface.
