from abc import ABC, abstractmethod

# Define an abstract base class called 'Vehicle'
class Vehicle(ABC):  # Inherits from ABC to make it an abstract class
    @abstractmethod
    def start_engine(self):
        # Abstract method for starting the engine
        # Subclasses must override this method with specific implementation
        pass

    @abstractmethod
    def stop_engine(self):
        # Abstract method for stopping the engine
        # Subclasses must override this method with specific implementation
        pass

# Define a concrete subclass of Vehicle called 'Car'
class Car(Vehicle):
    def start_engine(self):
        # Provide specific implementation for starting the car engine
        return "Car engine started."

    def stop_engine(self):
        # Provide specific implementation for stopping the car engine
        return "Car engine stopped."

# Instantiate the Car class
car = Car()
# Call the start_engine method on the Car object
print(car.start_engine())  # Output: Car engine started.
# Call the stop_engine method on the Car object
print(car.stop_engine())   # Output: Car engine stopped.
