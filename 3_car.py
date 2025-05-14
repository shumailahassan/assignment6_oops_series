#3. Public Variables and Methods: Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):        # public method
        print(self.brand, "car is starting...")

# Class ka object banate hain
my_car = Car("Toyota")

# Public variable access
print("Car Brand:", my_car.brand)

# Public method call
my_car.start()

