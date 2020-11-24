elements = input().split(' ')
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    index = elements[i + 1]
    bakery[key] = int(index)

print(bakery)