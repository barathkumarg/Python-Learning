# Content


## 1. Object Oriented Design
### Object-oriented Analysis
- Process of looking at the problem and identifying the objects.
- Outcome: Set of requirements.

e.g. Gathering the requirements to design the Website

### Object-oriented Design
- Process of converting the requirement into the implementation specification
- Outcome: Design stage, turning requirements into tasks

e.g. UI/UX Phase for the website

### Object-oriented Programming
- Process of converting the Design elements into working units, workable program
- Outcome: Set of Working Units

e.g. Creating the separate class and functions for the website design

## 2. OOPS Concepts

- Class : A Template contains the data members (Properties) and member functions

    e.g: A car blue print


- Object: Initialize the class (Using the common template of the class to define a new value)

    e.g: Initialize the car value according to the blue print


- Encapsulation: Aggregating the Data members and member functions

    e.g: Value and function in the car (speed, drive())


- Data Hiding: Making the Data members as private, public and protected

    e.g: Hiding internal gear mechanism in car


- Abstraction: Level of access, certain objects to access certain other objects (only certain and needed info be visible to end-user)

    e.g: Car class have access to only car components, Driver class have access only to the Action components


- Composition: Composition is a type of association where one object "owns" or "contains" another object, and the contained object cannot exist without the container object. It represents a strong relationship, and when the container object is destroyed, the contained objects are also destroyed.

    e.g:
    
    A Car "has an" Engine.
    The Engine is a part of the Car and cannot exist independently of the Car.  


- Association: Aggregation is a weaker form of association compared to composition. It indicates that one object "has" or "contains" another, but the contained object can exist independently of the container object. The lifecycle of the contained object is not tied to the container.

    e.g:
    
    A Car "has an" Driver.
    The Driver can exist independently of the Car. A driver can drive multiple cars, or even if the car is destroyed, the driver continues to exist.

- Polymorphism: Re-using the function or method on multiple situation
   
    e.g: do_action() to perform stop, start operations


- Inheritance: It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class.

## 3.Python Oops Implementation

### 3.1 Class and Object
Program
```python
class Car:
    ''' Class about car '''

    # class attribute
    car_type = "petrol"

    # Constructor, instance attributes
    def __init__(self, car_name):
        self.car_name = car_name

    # Instance Method
    def get_car_name(self):
        return self.car_name

    # Instance Method
    def set_car_name(self, car_name):
        self.car_name = car_name

    # str Method - textual representation of a object
    def __str__(self):
        return f'Car Name: {self.car_name}, Car Type: {Car.car_type}'

car = Car("Maruthi")
print(car)

# accessing the Class attribute
print(f'Car Type: {Car.car_type}' )
```

#### Self Parameter
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about. 

#### __init__() method
The __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated.

#### Class and Instance Variables

- Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class.

e.g: car_name

- Class variables are shared by all objects of a class and can be accessed using the class name

e.g: car_type

### 3.1 Inner Class

Program
```python
'''
Explains the python inner class concept
'''

class Outerclass:
    ''' Example for Outer - Inner class architecture '''

    def __init__(self):
        self.name = "Outerclass"
        self.inner = self.Innerclass() # attribute to the Inner class

    def show(self):
        print(f'It is: {self.name} ')

    # Inner class
    class Innerclass:
        def __init__(self):
            self.name = "Innerclass"
        
        def show(self):
            print(f'It is: {self.name}')

outerclass = Outerclass()
outerclass.show()
innerclass = outerclass.inner
innerclass.show()
```

#### Why inner class?
For the grouping of two or more classes. Suppose we have two classes remote and battery. Every remote needs a battery but a battery without a remote won’t be used. So, we make the Battery an inner class to the Remote. It helps us to save code. With the help of the inner class or nested class, we can hide the inner class from the outside world. Hence, Hiding the code is another good feature of the inner class.