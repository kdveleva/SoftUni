text = input()

while True:
    command = input()
    if "Travel" in command:
        print(f'Ready for world tour! Planned stops: {text}')
        break

    elif 'Add' in command:
        split_com = command.split(":")
        index = int(split_com[1])
        string = split_com[2]
        if 0 <= index < len(text):
            text = text[:index]+string+text[index:]

    elif 'Remove' in command:
        split_com = command.split(":")
        start_index = int(split_com[1])
        end_index = int(split_com[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text = text[:start_index] + text[end_index+1:]


    elif 'Switch' in command:
        split_com = command.split(":")
        old_str = split_com[1]
        new_str = split_com[2]
        text = text.replace(old_str, new_str)

    print(text)