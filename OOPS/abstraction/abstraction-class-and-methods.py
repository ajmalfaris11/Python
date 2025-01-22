from abc import ABC, abstractmethod

# Define an abstract base class called 'Animal'
class Animal(ABC):  # ABC ensures this is an abstract class and cannot be instantiated
    @abstractmethod
    def make_sound(self):
        # Abstract method that must be implemented by all subclasses
        pass

# Concrete subclass of Animal implementing the abstract method
class Dog(Animal):
    def make_sound(self):
        # Provide the specific implementation of the abstract method for 'Dog'
        return "Bark"

# Another concrete subclass of Animal implementing the abstract method
class Cat(Animal):
    def make_sound(self):
        # Provide the specific implementation of the abstract method for 'Cat'
        return "Meow"

# Instantiate the 'Dog' class (concrete subclass)
dog = Dog()
# Call the 'make_sound' method specific to the Dog class
print(dog.make_sound())  # Output: Bark

# Instantiate the 'Cat' class (concrete subclass)
cat = Cat()
# Call the 'make_sound' method specific to the Cat class
print(cat.make_sound())  # Output: Meow

# Attempting to instantiate the abstract base class directly would result in an error:
# animal = Animal()  # This line is commented because it raises a TypeError
