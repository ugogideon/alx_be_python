# main.py

from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # Create a list of different shapes
    shapes = [
        Rectangle(10, 5),  # Create a Rectangle instance with length 10 and width 5
        Circle(7)          # Create a Circle instance with radius 7
    ]

    # Loop through the shapes and print their respective areas using polymorphism
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
