#10. Instance Method: Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance variable
        self.breed = breed    # instance variable

    def bark(self):
        print(f"{self.name} is barking!")

# Object
dog1 = Dog("Buddy", "Labrador")

# Method call
dog1.bark()
