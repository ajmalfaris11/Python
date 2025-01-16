class Cars:  # when create a class, class name should be camel case
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

    def start(self):
        print(self.name + " Engine Started")


car1 = Cars("Maruti Swift", 100000, "Red")
car2 = Cars("Toyota Innova", 200000, "Black")

print(car1.name, car1.price, car1.colour)
print(car2.name, car2.price, car2.colour)

car1.start()
car2.start()


#  update car1 property ---> car1.property = updated value
#  delete the object ---> del car2