key = input()
while True:
    command = input().split(">>>")
    if command[0] == 'Generate':
        break
    elif command[0] == "Contains":
        substring = command[1]
        if substring in key:
            print(f'{key} contains {substring}')
        else:
            print(f'Substring not found!')
    elif command[0] == 'Flip':
        upper_lower = command[1]
        start = int(command[2])
        end = int(command[3])
        if upper_lower == "Upper":
            new_key = key[start:end].upper()
            key = key[:start]+new_key+key[end:]
            print(key)
        elif upper_lower == "Lower":
            new_key = key[start:end].lower()
            key = key[:start]+new_key+key[end:]
            print(key)
    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        key = key[:start]+key[end:]
        print(key)

print(f'Your activation key is: {key}')