n = int(input())
plants = {}
ratings = {}

for _ in range(n):
    text = input().split("<->")
    plant = text[0]
    rarity = int(text[1])
    if plant not in plants:
        plants[plant] = {'Rarity:': 0, 'Rating:': 0.00}
    plants[plant]['Rarity:'] = rarity

while True:
    command = input().split(" ")
    action = command[0]
    if action == 'Exhibition':
        break
    elif action == 'Rate:':
        plant = command[1]
        rating = int(command[3])
        if plant not in ratings:
            ratings[plant] = []
        ratings[plant].append(rating)
    elif action == 'Update:':
        plant = command[1]
        rarity = int(command[3])
        plants[plant]['Rarity:'] = rarity
    elif action == 'Reset:':
        plant = command[1]
        ratings[plant] = [0.00]
    else:
        print('error')

for k, v in ratings.items():
    if v != 0:
        plants[k]['Rating:'] = abs(sum(v) / len(v))
    else:
        plants[k]['Rating:'] = 0.00


plants = dict(sorted(plants.items(), key=lambda x: ((-x[1]["Rarity:"]), (-x[1]["Rating:"]))))
print(f'Plants for the exhibition:')
for key, value in plants.items():
    print(f'- {key}; Rarity: {value["Rarity:"]}; Rating: {value["Rating:"]:.2f}')

