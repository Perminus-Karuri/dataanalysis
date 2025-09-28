class Vehicle:
    def __init__(self, make, model):  # properties of the vehicle class
        self.make = make
        self.model = model

    def moves(self):  # method of what the vehicle does
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle("Mazda", "Atenza")  # object created from class vehicle

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Subaru", "Forester")
your_car.get_make_model()
your_car.moves()

# Inheritance

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):  # properties of the airplane class
        super().__init__(make, model) # inherits from the parent vehicle
        self.faa_id = faa_id

    def moves(self):
        print("Flies along...")

    def get_make_model(self):  # Override the parent method
        print(f"I'm a {self.make} {self.model} with FAA ID: {self.faa_id}")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
    pass

cessna = Airplane("Cessna", "Skyhawk", "N-1234")
my_truck = Truck("Mercedes", "Actros")
golfwagon = GolfCart("Yamaha", "GC200")

cessna.get_make_model()
cessna.moves()

my_truck.get_make_model()
my_truck.moves()

golfwagon.get_make_model()
golfwagon.moves()

print("\n\n")

# Polymorphism - ability to behave differently/ take many forms

for v in (my_car, your_car, cessna, my_truck, golfwagon):
    v.get_make_model()
    v.moves()
    