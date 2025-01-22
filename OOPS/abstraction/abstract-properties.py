from abc import ABC, abstractmethod

# Define an abstract base class called 'Shape'
class Shape(ABC):  # Inherits from ABC to make it an abstract class
    @property
    @abstractmethod
    def area(self):
        # Abstract property method to calculate the area
        # Subclasses must override this method and provide an implementation
        pass

# Define a concrete subclass of Shape called 'Rectangle'
class Rectangle(Shape):
    def __init__(self, width, height):
        # Initialize the width and height of the rectangle
        self.width = width
        self.height = height

    @property
    def area(self):
        # Override the abstract 'area' property
        # Calculate and return the area of the rectangle
        return self.width * self.height

# Instantiate the Rectangle class with specific dimensions
rect = Rectangle(5, 10)
# Access the 'area' property, which calculates and returns the area
print(rect.area)  # Output: 50
