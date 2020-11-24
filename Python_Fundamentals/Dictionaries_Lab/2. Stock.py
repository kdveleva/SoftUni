elements = input().split(' ')
search_for = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    index = elements[i + 1]
    bakery[key] = int(index)

for product in search_for:
    if product in bakery:
        print(f'We have {bakery[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
