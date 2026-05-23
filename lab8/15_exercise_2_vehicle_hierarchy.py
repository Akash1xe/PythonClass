class Vehicle:
    def vehicle_type(self):
        print("This is a Vehicle")


class Car(Vehicle):
    def car_name(self):
        print("Car : BMW")


class Bike(Vehicle):
    def bike_name(self):
        print("Bike : Royal Enfield")


c = Car()
b = Bike()

c.vehicle_type()
c.car_name()

b.vehicle_type()
b.bike_name()
