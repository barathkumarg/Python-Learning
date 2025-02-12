# Single Inheritance

class Animal():
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print(self.name," is an Animal!")
    
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name) # call the parent class
    
    
dog = Dog("Puppy")
dog.display() # "Puppy is an Animal"

# Multiple Inheritance

class Camera():
    def __init__(self,name,pixel):
        self.name=name
        self.pixel=pixel
        
class Battery():
    def __init__(self,name,power):
        self.name=name
        self.power=power
        
class Phone(Battery, Camera):
    def __init__(self, battery, cname, pixel):
        self.battery = battery
        self.camera = Camera(cname, pixel)

    def displayDetails(self):
        print("This phone  has power of",self.battery.power,self.battery.name,"battery and",self.camera.name," camera with",self.camera.pixel)
     
  
phone = Phone(Battery('5500mAh','SnapDragon'), 'Sony', '50MP')
phone.displayDetails() # "This phone  has power of SnapDragon 5500mAh battery and Sony  camera with 50MP" 

#Multilevel Inheritance

class GrandParent():
    def __init__(self,name):
        self.name= name
        
class Parent(GrandParent):
    def __init__(self,name,fatherName):
        self.grandparent = GrandParent(fatherName)
        self.name= name
        
class Children(Parent):
    def __init__(self,name,fatherName, GrandParentName):
        self.parent = Parent(fatherName,GrandParentName)
        self.name= name
        
    def display(self):
        print("I am",self.name,"this is my father,",self.parent.name,"and this is my GrandParent", self.parent.grandparent.name,". I love to dance" )
        
children = Children("A","B","C")
children.display()

#Hierarchical Inheritance

class Children2(Parent):
    def __init__(self,name,fatherName, GrandParentName):
        self.parent = Parent(fatherName,GrandParentName)
        self.name= name
        
    def display(self):
        print("I am",self.name,"this is my father,",self.parent.name,"and this is my GrandParent", self.parent.grandparent.name,". I love to sing" )
        
children2 = Children2("D","B","C")
children2.display()

#Hybrid Inheritance

class Vehicle:
    def __init__(self, name):
        self.name = name

class Car(Vehicle):
    def __init__(self, name, speed):
        Vehicle.__init__(self,name)
        self.speed = speed
        print(f"Car initialized: {self.name}, {self.speed} km/h")

class Boat(Vehicle):
    def __init__(self, name, capacity):
        Vehicle.__init__(self,name)
        self.capacity = capacity
        print(f"Boat initialized: {self.name}, {self.capacity} passengers")

class AmphibiousVehicle(Car, Boat):
    def __init__(self, name, speed, capacity):
        Car.__init__(self, name, speed)
        Boat.__init__(self, name, capacity)
        print(f"AmphibiousVehicle initialized: {self.name}, {self.speed} km/h, {self.capacity} passengers")

amphibious = AmphibiousVehicle("AmphiCar", 80, 4)
    

