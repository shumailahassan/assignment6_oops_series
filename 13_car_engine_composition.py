#13. Composition: Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

# Engine class
class Engine:
    def start(self):
        print("Engine started")

# Car class
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        # Car ke zariye engine ka method call ho raha hai
        self.engine.start()

# Engine object create karo
my_engine = Engine()

# Engine object pass karo Car class me (composition)
my_car = Car(my_engine)

# Car ka method call karo, jo engine ko start karega
my_car.start_car()
