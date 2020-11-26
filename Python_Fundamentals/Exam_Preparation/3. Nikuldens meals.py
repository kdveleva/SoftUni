guest_book = {}
unliked_meals = []
while True:
    command = input().split('-')
    action = command[0].lower()
    if action == 'stop':
        break
    elif action == 'like':
        guest = command[1]
        meal = command[2]
        if guest not in guest_book:
            guest_book[guest] = []
        elif meal in guest_book[guest]:
            continue
        guest_book[guest].append(meal)

    elif action == 'unlike':
        guest = command[1]
        meal = command[2]
        if guest not in guest_book:
            print(f"{guest} is not at the party.")
        elif meal not in guest_book[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            guest_book[guest].remove(meal)
            unliked_meals.append(meal)
            print(f"{guest} doesn't like the {meal}.")

guest_book = dict(sorted(guest_book.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in guest_book.items():
    print(f'{key}: {", ".join(value)}')
print(f'Unliked meals: {len(unliked_meals)}')