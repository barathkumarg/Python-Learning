'''

Explains about the class and python objects
'''

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
print(f'Car Type: {Car.car_type}')


