text = input()
while True:
    command = input().split(' ')
    if command[0] == "Finish":
        break
    elif command[0] == 'Replace':
        current_char = command[1]
        new_char = command[2]
        text = text.replace(current_char, new_char)
        print(text)
    elif command[0] == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index >= len(text) or end_index >= len(text)\
                or start_index < 0 or end_index < 0:
            print("Invalid indexes!")
            continue
        substring = text
        text = text[:start_index]+text[end_index+1:]
        print(text)
    elif command[0] == "Make":
        if command[1] == "Upper":
            text = text.upper()
            print(text)
        elif command[1] == "Lower":
            text = text.lower()
            print(text)
    elif command[0] == "Check":
        string = command[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        ascii_index_sum = 0
        if start_index >= len(text) or end_index >= len(text)\
                or start_index < 0 or end_index < 0:
            print("Invalid indexes!")
            continue
        substring = text[start_index:end_index+1]
        for letter in substring:
            ascii_index_sum += ord(letter)
        print(ascii_index_sum)