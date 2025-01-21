class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self._department = "IT"  # Protected attribute
        self.__salary = salary  # Private attribute

    # Getter for private attribute
    def get_salary(self):
        return self.__salary

    # Setter for private attribute
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

# Creating an instance of the Employee class
emp = Employee("Alice", 50000)

# Accessing public attribute
print(emp.name)  # Output: Alice

# Accessing protected attribute (not recommended directly)
print(emp._department)  # Output: IT

# Accessing private attribute (throws error if accessed directly)
# print(emp.__salary)  # Uncommenting this line will raise an AttributeError

# Using getter and setter methods for private attribute
print(emp.get_salary())  # Output: 50000
emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000
