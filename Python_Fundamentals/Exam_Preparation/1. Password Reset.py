text = input()
new_password = ''
while True:
    command = input().split(' ')
    action = command[0]
    if action == 'Done':
        break
    elif action == "TakeOdd":
        for index in range(len(text)):
            if index % 2 != 0:
                new_password += text[index]
        text = new_password
        print(text)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        text = text[:index] + text[index+length:]
        print(text)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print('Nothing to replace!')

print(f'Your password is: {text}')