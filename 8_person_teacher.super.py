#8. The super() Function: Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor



# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # super() se base class ka constructor call ho raha
        self.subject = subject

#object
teacher1 = Teacher("Ali", "Math")
print("Name:", teacher1.name)
print("Subject:", teacher1.subject)
