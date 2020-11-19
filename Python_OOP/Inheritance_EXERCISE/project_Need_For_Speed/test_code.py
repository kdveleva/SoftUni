from project_Need_For_Speed.car import Car
from project_Need_For_Speed.cross_motorcycle import CrossMotorcycle
from project_Need_For_Speed.motorcycle import Motorcycle
from project_Need_For_Speed.race_motorcycle import RaceMotorcycle
from project_Need_For_Speed.sport_car import SportCar
from project_Need_For_Speed.vehicle import Vehicle
from project_Need_For_Speed.family_car import FamilyCar

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
# print(vehicle.drive(10))
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)


def if_inheritance_is_correct():
    for kls in [Car, CrossMotorcycle, FamilyCar, Motorcycle, RaceMotorcycle, SportCar, Vehicle]:
        parent = kls.__mro__[1].__name__
        class_name = kls.__name__
        print(kls.__class__.__name__, kls.__mro__[1].__name__)
