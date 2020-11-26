skill = input()
while True:
    command = input().split(' ')
    if command[0] == "For":
        break
    elif command[0] == "GladiatorStance":
        skill = skill.upper()
        print(skill)
    elif command[0] == 'DefensiveStance':
        skill = skill.lower()
        print(skill)
    elif command[0] == 'Dispel':
        index = int(command[1])
        letter = command[2]
        if index >= len(skill):
            print('Dispel too weak.')
            continue
        skill = skill[:index]+letter+skill[index+1:]
        print('Success!')
    elif command[0] == 'Target':
        if len(command) < 2:
            print("Command doesn't exist")
            continue
        if command[1] == "Change":
            substring = command[2]
            second_substring = command[3]
            skill = skill.replace(substring, second_substring)
            print(skill)
        elif command[1] == "Remove":
            substring = command[2]
            skill = skill.replace(substring, "")
            print(skill)
        else:
            print("Command doesn't exist!")

    else:
        print("Command doesn't exist!")