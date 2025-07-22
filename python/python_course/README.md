### OOP
#### Objects
- Objects are defined in pascal case
```python
timmy = turtle.Turtle()
```
with parentheses
- Classes are a blueprint for creating objects.
- Attributes are accessed using the pattern `object.attribute`
```python
car.speed
```
- Objects have functions associated with them, known as methods: `car.stop()`
#### Classes
- Just a blueprint for making an object
- Syntax:
- ```python
class CarWithPulley:
```
This is particular kind of casing called PascalCase in which EVERY letter is capitalized.  camelCase has the first letter lower
- You can add attributes to classes just by using the dot notation.  Even if the class doesn't have the attribute in-built, you can still flexibly add information to an object
```python
class User:
    pass

user_1 = User()
user_1.username = "axman13"
print(user_1.username)
```
this is totally valid and will work.
- Constructors
  - Also known as initializing a object.  It allows you to set the initial values of attributes.
  - The `__init__` function does just that.  It gets called everytime you make a new object from the class it's defined in
```python
class Car:
    def __init__(self, seats):
        print("New Car being created...")
        self.seats = seats
my_car = Car(5) # Sets the seats attribute as 5
```
- Methods
  - Like function within an object.  It allows you to automatically act on your object or do other things with your object.
```python
class Car:
    def __init__(self, seats):
        print("New Car being created...")
        self.seats = seats
    def enter_race_mode():
      self.seats = 2
```

### Importing modules
#### Styles
```python
import module
from module import class
import module as m
```

### Event Listeners
- Functions that look out for things that happen

### Higher Order Functions
- Functions that take other funcitons as arguments
```python
def higher_order_function(function, other_arg):
  x = function(other_arg)
  return x
```