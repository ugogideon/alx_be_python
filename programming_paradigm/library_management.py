#library_management.py
class Book:
    """Represents a book in the library."""
    def __init__(self, title, author):
        """Initialize the book with title, author, and its availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def return_book(self):
        """Mark the book as available (checked in)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out
class Library:
    """Represents a collection of books and manages them."""
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store Book instances
    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)
    def check_out_book(self, title):
        """Check out a book by its title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out '{title}'")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' is not available or does not exist in the library.")
    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                return
        print(f"'{title}' is not currently checked out or does not exist in the library.")
    def list_available_books(self):
        """Print a list of books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books in the library.")
                                