# Library Management System
# Create classes for Book and Library. Add methods to borrow and return books.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
 
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.is_available:
                print(f"- {book.title} by {book.author}")
        print()
 
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f"You borrowed: {book.title}")
                return
        print("Book not available.")
 
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                print(f"You returned: {book.title}")
                return
        print("Book was not borrowed or does not belong to this library.")

library = Library()

library.add_book(Book("The Alchemist", "Paulo Coelho"))
library.add_book(Book("Wings of Fire", "A.P.J Abdul Kalam"))
library.add_book(Book("Harry Potter", "J.K. Rowling"))

library.show_books()

library.borrow_book("Harry Potter")

library.borrow_book("Harry Potter")

library.return_book("Harry Potter")

library.show_books()

 