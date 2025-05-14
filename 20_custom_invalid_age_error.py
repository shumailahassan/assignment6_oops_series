#20. Creating a Custom Exception:Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom exception class
class InvalidAgeError(Exception): #Raised when age is less than 18
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")
    else:
        print("Access granted!")

# Try-Except block to handle the exception
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
