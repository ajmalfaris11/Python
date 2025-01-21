# Polymorphism with Inheritance (Method Overriding)
# ++++++++++++++++++++++++++++++++++++++++++++++++++

class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Demonstrating polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())
