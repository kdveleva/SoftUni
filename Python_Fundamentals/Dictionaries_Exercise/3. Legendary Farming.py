from collections import defaultdict


# def print_result(results):
#     for m, q in results.items():
#         return f'{m}: {q}'


key_material = {'shards': 0, 'fragments': 0, 'motes': 0}
materials = defaultdict(int)
price = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
is_won = False

while True:
    if is_won:
        break
    command = input().lower()
    material = command.split(' ')
    for i in range(0, len(material), 2):
        quantity = int(material[i])
        material_type = material[i + 1]
        # adding key materials
        if material_type in key_material:
            key_material[material_type] += quantity
            if key_material[material_type] > 249:
                key_material[material_type] -= 250
                print(f'{price[material_type]} obtained!')
                is_won = True
                break
        else:
            materials[material_type] += quantity

key_material = dict(sorted(key_material.items(), key=lambda x: (-x[1], x[0])))
materials = dict(sorted(materials.items(), key=lambda x: x[0]))

for m, q in key_material.items():
    print(f'{m}: {q}')
for m, q in materials.items():
    print(f'{m}: {q}')
