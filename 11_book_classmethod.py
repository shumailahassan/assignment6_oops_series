 #11. Class Methods: Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added

class Book:
    total_books = 0  # class variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # class variable ko update karo

Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()

# Total books count print karo
print("Total books added:", Book.total_books)



