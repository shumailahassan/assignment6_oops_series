#1. Using self: Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self, name, marks):
        self.name = name    # instance variable
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks:{self.marks}")

# object
student1 = Student("Shumaila", 92)
student1.display()

