def sail(data_dict):
    while True:
        command = input().split("||")
        if command[0] == "Sail":
            break
        cities, population, gold = command
        if cities not in data_dict:
            data_dict[cities] = [0, 0]
        data_dict[cities][0] += int(population)
        data_dict[cities][1] += int(gold)
    return data_dict


sail_dictionary = {}
sail(sail_dictionary)

while True:
    command = input().split("=>")
    if command[0] == "End":
        break
    elif command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        sail_dictionary[town][0] -= people
        sail_dictionary[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if sail_dictionary[town][0] <= 0 or sail_dictionary[town][1] <= 0:
            sail_dictionary.pop(town)
            print(f'{town} has been wiped off the map!')

    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
            continue
        sail_dictionary[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {sail_dictionary[town][1]} gold.")
sail_dictionary = dict(sorted(sail_dictionary.items(), key=lambda x:(-x[1][1], x[0])))

if len(sail_dictionary) > 0:
    print(f'Ahoy, Captain! There are {len(sail_dictionary)} wealthy settlements to go to:')
    for key, value in sail_dictionary.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')

