
orders_dict = {}

while True:
    command = input()
    if command == 'buy':
        break
    items = command.split(' ')
    name = items[0]
    price = float(items[1])
    quantity = int(items[2])
    if name not in orders_dict:
        orders_dict[name] = [price, quantity]
    else:
        orders_dict[name][0] = price
        orders_dict[name][1] += quantity

for key, value in orders_dict.items():
    orders_dict[key] = value[0] * value[1]

for key, value in orders_dict.items():
    print(f'{key} -> {value:.2f}')
