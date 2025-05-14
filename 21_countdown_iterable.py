#21. Make a Custom Class Iterable: Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start          # Store the original starting number
        self.current = start        # Used for counting down

    def __iter__(self):
        return self                 # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration     # Stop when it goes below 0
        num = self.current
        self.current -= 1           # Count down by 1
        return num

# Test the Countdown
c = Countdown(7)

for number in c:
    print(number)
