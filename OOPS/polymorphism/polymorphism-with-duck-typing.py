#  Polymorphism with Duck Typing
# ++++++++++++++++++++++++++++++

class Car:
    def start(self):
        print("Car is starting...")

class Bike:
    def start(self):
        print("Bike is starting...")

def start_vehicle(vehicle):
    vehicle.start()

# Passing objects of different types
start_vehicle(Car())
start_vehicle(Bike())
