from abc import ABC, abstractmethod

# Define an abstract base class called 'Appliance'
class Appliance(ABC):  # Inherits from ABC to make it an abstract class
    def plug_in(self):
        # Concrete method for plugging in the appliance
        # This method can be directly used by any subclass
        return "Plugged in!"

    @abstractmethod
    def operate(self):
        # Abstract method for operating the appliance
        # Subclasses must override this method with specific functionality
        pass

# Define a concrete subclass of Appliance called 'WashingMachine'
class WashingMachine(Appliance):
    def operate(self):
        # Provide specific implementation for the 'operate' method
        # Describes the operation of a washing machine
        return "Washing clothes."

# Instantiate the WashingMachine class
machine = WashingMachine()
# Call the 'plug_in' method (inherited from the Appliance class)
print(machine.plug_in())   # Output: Plugged in!
# Call the 'operate' method (implemented in the WashingMachine class)
print(machine.operate())   # Output: Washing clothes.
