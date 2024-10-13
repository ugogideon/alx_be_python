# book_class.py

class Book:
    """A class representing a book."""
    
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation of the Book for user-friendly output."""
        return f"{self.title} by {self.author}, published in {self.year}"

     def __repr__(self):
         """Return an official string representation of the Book for debugging."""
         return f"Book('{self.title}', '{self.author}', {self.year})"
