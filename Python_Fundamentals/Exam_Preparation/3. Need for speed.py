# from collections import defaultdict
n = int(input())
car_dict = {}
for i in range(n):
    cars = input().split('|')
    car, mileage, fuel = cars
    if car not in car_dict:
        car_dict[car] = []
    car_dict[car].append(int(mileage))
    car_dict[car].append(int(fuel))

while True:
    commands = input().split(" : ")
    action = commands[0]
    if action == "Stop":
        break
    elif action == "Drive":
        drive, car_type, distance, fuel = commands
        if car_dict[car_type][1] < int(fuel):
            print('Not enough fuel to make that ride')
        else:
            car_dict[car_type][0] += int(distance)
            car_dict[car_type][1] -= int(fuel)
            print(f'{car_type} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if car_dict[car_type][0] > 99999:
            car_dict.pop(car_type)
            print(f'Time to sell the {car_type}!')

    elif action == "Refuel":
        refuel, car, add_fuel = commands
        car_dict[car][1] += int(add_fuel)
        if car_dict[car][1] > 74:
            add_fuel = abs((car_dict[car][1] - 75) - int(add_fuel))
            car_dict[car][1] = 75
        print(f"{car} refueled with {add_fuel} liters")

    elif action == "Revert":
        revert, car, kilometers = commands
        car_dict[car][0] -= int(kilometers)
        if car_dict[car][0] < 10000:
            car_dict[car][0] = 10000
            continue
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')

car_dict = dict(sorted(car_dict.items(), key=lambda x: (-x[1][0], x[0])))
for key, value in car_dict.items():
    print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')
