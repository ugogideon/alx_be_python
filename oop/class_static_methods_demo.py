# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """A static method that adds two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """A class method that multiplies two numbers and prints the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
