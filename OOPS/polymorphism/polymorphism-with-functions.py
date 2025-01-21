# Polymorphism with Functions
# +++++++++++++++++++++++++++

class Rectangle:
    def area(self, length, width):
        return length * width

class Circle:
    def area(self, radius):
        return 3.14 * radius * radius

# Using the same function name `area`
shapes = [Rectangle(), Circle()]

# Calculate areas
print(shapes[0].area(5, 10))  # Rectangle area
print(shapes[1].area(7))      # Circle area