#19. callable() and __call__():Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # store the multiplication factor

    def __call__(self, number):
        return number * self.factor  # makes the object callable like a function


# Create an object with a factor
m = Multiplier(7)

# Check if the object is callable
print("Is the object callable?", callable(m))

# Call the object like a function
print("4 * 7 =", m(4))   
print("10 * 7 =", m(10)) 
print("2 * 7 =", m(2))  
