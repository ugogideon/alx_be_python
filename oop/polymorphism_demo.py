# polymorphism_demo.py

import math

class Shape:
    """A base class representing a general shape."""

    def area(self):
        """Method to calculate the area of a shape. Should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area method")

class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""

    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle (length × width)."""
        return self.length * self.width

class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize a circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle (π × radius²)."""
        return math.pi * (self.radius ** 2)
