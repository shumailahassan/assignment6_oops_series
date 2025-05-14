#18. Property Decorators: @property, @setter, and @deleter:Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            print("Setting the price...")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Create an object
p = Product(100)

# Get the price
print(p.price)

# Set a new price
p.price = 200  
p.price = -50   #  Price cannot be negative!
print(p.price)

del p.price     # Deletes the _price attribute
