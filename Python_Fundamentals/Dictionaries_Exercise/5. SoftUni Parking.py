num_commands = int(input())
parking = {}

for _ in range(num_commands):
    commands = input().split(' ')
    action = commands[0]
    name = commands[1]

    if action == "register":
        license_plate = commands[2]
        if name not in parking:
            parking[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif action == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")

for key, value in parking.items():
    print(
        f'{key} => {value}'
    )
