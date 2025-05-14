#9. Abstract Classes and Methods: Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().



from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 9)
print("Area of rectangle:", rect.area())
