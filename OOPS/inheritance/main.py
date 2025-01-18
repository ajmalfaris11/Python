#  Parent Class
class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def address(self):
        print(self.name, self.contact)



#  Child Class
class Doctor(Person):
    # if we inherit the parent class we should need a methods or property other ways use "pass" keyword
    pass

class Patient(Person):
    pass

doc1 = Doctor("Ajmal", 1234)
part1 = Patient("Faris", 5678)

doc1.address()
part1.address()