#2. Using cls: Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1  # har object banne par count barhta hai

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

# Objects create karte hain
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Class method call karte hain
Counter.show_count()

