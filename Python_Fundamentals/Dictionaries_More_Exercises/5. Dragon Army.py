from collections import defaultdict
dragons = defaultdict(list)
statistics = {'damage': 45, 'health': 250, 'armor': 10}

num = int(input())
for _ in range(num):
    command = input().split(' ')
    dragon_type = command[0]
    dragon_name = command[1]
    damage = command[2]
    health = command[3]
    armor = command[4]
    if dragon_name in dragons[dragon_name]:
        continue
    else:
        dragons[dragon_type].append(dragon_name)

