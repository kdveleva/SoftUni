from collections import defaultdict
force_book = defaultdict(list)
user_exists = False
while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        command = command.split(' | ')
        force_side = command[0]
        force_user = command[1]
        for user in force_book.values():
            if force_user in user:
                user_exists = True
        if not user_exists:
            force_book[force_side].append(force_user)
    elif "->" in command:
        command = command.split(' -> ')
        force_side = command[1]
        force_user = command[0]

        for side, user in force_book.items():
            if force_user in user:
                force_book[side].remove(force_user)

        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

sort_dict = dict(sorted(force_book.items(), key=lambda v: (-len(v[1]), v[0])))

for key, value in sort_dict.items():
    if len(value) == 0:
        continue
    print(f'Side: {key}, Members: {len(value)}')
    for item in sorted(value):
        print(f'! {item}')
