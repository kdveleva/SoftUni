products_in_stock = {}

while True:
    command = input()
    if command == 'statistics':
        break

    products = command.split(": ")
    product = products[0]
    quantity = int(products[1])
    if product not in products_in_stock:
        products_in_stock[product] = 0
    products_in_stock[product] += quantity

print('Products in stock:')
for k, i in products_in_stock.items():
    print(f'- {k}: {i}')
print(f'Total Products: {len(products_in_stock.keys())}')
print(f'Total Quantity: {sum(products_in_stock.values())}')
