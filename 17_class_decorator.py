#17. Class Decorators:Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.



# Class decorator banaya
def add_greeting(cls):  # cls ka matlab hai: class jisko decorate karna hai
    def greet(self):  # yeh method hum class ke andar inject kar rahe hain
        return "Hello from Decorator!"

    cls.greet = greet  # class me naya method greet add kar diya
    return cls  # modified class ko wapas return kar diya

# Person class banayi aur uspe decorator lagaya
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Object banaya Person ka
p = Person("Ali")

# Ab greet method available hai
print(p.greet())  # Output: Hello from Decorator!
