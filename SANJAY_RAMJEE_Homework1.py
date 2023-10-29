import math

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'({self.x},{self.y})'
class Car:
    def __init__(self, car_name, location, cost_per_mile):
        self.car_name = car_name
        self.location = location
        self.cost_per_mile = cost_per_mile
    def __str__(self):
        return f'[{self.car_name} , {self.location}, {self.cost_per_mile}]'
    
    def move_to(self, new_x, new_y):
        self.location.x = new_x
        self.location.y = new_y
    

    
class Passenger:
    def __init__(self, passenger_name, location):
        self.passenger_name = passenger_name
        self.location = location
    def __str__(self):
        return f'[{self.passenger_name}, {self.location}]'
    def move_to(self, new_x, new_y):
        self.location.x = new_x
        self.location.y = new_y

    
        
    
class RideSharingApp:
    def __init__(self):
        self.cars = []
        self.passengers = []

    def add_car(self, car):
        self.cars.append(car)
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    def remove_car(self, car):
        self.cars.remove(car)
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)
    def find_cheapest_car(self, passenger):
        cost = 10000000000
        for car in self.cars:
            if car.cost_per_mile < cost:
                cost = car.cost_per_mile
                cheapest_car = car

        print(f'The cheapest car for {passenger.passenger_name} is {cheapest_car.car_name}, Cost per mile: {cost}')
    def find_nearest_car(self, passenger):
        self.passenger_x = passenger.location.x
        self.passenger_y = passenger.location.y
        min_distance = 10000000000
        for car in self.cars:
            carx = car.location.x
            cary = car.location.y

            distance = math.sqrt(((carx - self.passenger_x) ** 2) + ((cary - self.passenger_y) ** 2))
            distance = round(distance, 2)
            if distance < min_distance:
                min_distance = distance
                nearest_car = car
        print(f'The nearest car for {passenger.passenger_name} is {nearest_car.car_name}, Distance: {min_distance}')

        






        
    

#For the remaining code (after this line), no modification is required
print('---------------------Object creation------------------')
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 0.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)

location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)

mobileApp = RideSharingApp()
mobileApp.add_car(car1)
mobileApp.add_car(car2)
mobileApp.add_passenger(passenger1)
mobileApp.add_passenger(passenger2)

print('-----------------------Scenario 1---------------------')
mobileApp.find_cheapest_car(passenger1)
mobileApp.find_cheapest_car(passenger2)
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 2---------------------')
car1.move_to(0,-5)
passenger1.move_to(0,3)
print('car1\'s location has been updated:',car1)
print('passenger1\'s location has been updated:', passenger1)

mobileApp.find_cheapest_car(passenger1)
mobileApp.find_cheapest_car(passenger2)
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 3---------------------')
car3= Car('car3', Location(0,2), 0.3)
mobileApp.add_car(car3)
print('New car added:',car3)
mobileApp.find_cheapest_car(passenger1)
mobileApp.find_cheapest_car(passenger2)
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

