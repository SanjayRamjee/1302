class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        string = f'Make: {self.make} model: {self.model} year: {self.year}'
        return string

    def __lt__(self, other):
        if self.year < other.year:
            return True
        else:
            return False

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        Vehicle.__init__(self, make, model, year)
        self.num_doors = num_doors

    def honk(self):
        print('"Honk! Honk! From Car".')

    def get_info(self):
        string = f'Make: {self.make} model: {self.model} year: {self.year} num_doors {self.num_doors}'
        return string

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type):
        Vehicle.__init__(self, make, model, year)
        self.type = type

    def honk(self):
        print('"Honk! Honk! From Motorcycle".')

    def get_info(self):
        string = f'Make: {self.make} model: {self.model} year: {self.year} type: {self.type}'
        return string

class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        Vehicle.__init__(self, make, model, year)
        self.capacity = capacity

    def honk(self):
        print('"Honk! Honk! From Truck".')

    def get_info(self):
        string = f'Make: {self.make} model: {self.model} year: {self.year} capacity: {self.capacity}'
        return string

    def __lt__(self, other):
        return self.capacity < other.capacity

class PickupTruck(Car, Truck):
    def __init__(self, make, model, year, num_doors, capacity, has_cover):
        Car.__init__(self, make, model, year, num_doors)
        Truck.__init__(self, make, model, year, capacity)  
        self.has_cover = has_cover

    def get_info(self):
        string = f'Make: {self.make} model: {self.model} year: {self.year} num_doors: {self.num_doors} capacity: {self.capacity} has cover: {self.has_cover}'
        return string

    def honk(self):
        return Car.honk(self)

c1 = Car('Audi', 'a4', 2014, 4)
m1 = Motorcycle("African Twin", "DX", 2018, "Standard")
t1 = Truck("Optimus Prime", "Autobot", 2012, 500)
pT1 = PickupTruck("Chevrolet", "Silverado", 2020, 6, 400, True)

c1.honk()
m1.honk()
t1.honk()
pT1.honk()

print(c1.get_info())
print(m1.get_info())
print(t1.get_info())
print(pT1.get_info())

print(t1 < pT1)
