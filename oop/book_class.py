# book_class.py

class Book:
    """A class representing a book with title, author, and publication year."""
    
    def __init__(self, title, author, year):
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that is called when an object is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

     def __repr__(self):
        """Return an official string representation of the Book for debugging."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
