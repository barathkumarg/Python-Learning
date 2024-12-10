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

