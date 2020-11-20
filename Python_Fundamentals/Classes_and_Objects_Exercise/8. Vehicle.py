class Vehicle:

    def __init__(self, type, model, price):
        self.price = price
        self.model = model
        self.type = type
        self.owner = None
        
    def buy(self, money, owner):
        if owner is not None:
            return 'Car already sold'
        elif money >= self.price:
            change = money - self.price
            return f'Successfully bought a {self.type}. Change: {change}'
        else:
            return 'Sorry, not enough money'

    def sell(self):
        pass

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        return f"{self.model} {self.type} is owned by: {self.owner}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
