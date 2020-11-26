concealed_message = input()
message = concealed_message
reversed_string = False
while True:
    commands = input()
    if commands == "Reveal":
        print(f'You have a new text message: {"".join(message)}')
        break
    command = commands.split(":|:")
    action = command[0]
    if action == 'InsertSpace':
        space = int(command[1])
        message = message[:space] + " " + message[space:]
        print(message)
    elif action == 'Reverse':
        substring = command[1]
        if substring not in message:
            print("error")
        else:
            if not reversed_string:
                message = message.replace(substring, "", 1)
                message += substring[::-1]
                reversed_string = True
                print("".join(message))
    elif action == 'ChangeAll':
        letter_to_be_replaced = command[1]
        replacement = command[2]
        if letter_to_be_replaced in message:
            message = message.replace(letter_to_be_replaced, replacement)
            print("".join(message))