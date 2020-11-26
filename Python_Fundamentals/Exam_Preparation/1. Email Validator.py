email = input()
while True:
    command = input().split()
    action = command[0].lower()
    if action == 'complete':
        break
    elif action == 'make':
        if command[1].lower() == 'upper':
            email = email.upper()
            print(email)
        else:
            email = email.lower()
            print(email)
    elif action == 'getdomain':
        count = int(command[1])
        print(f'{email[-count:]}')
    elif action == 'getusername':
        if '@' not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            index = email.index('@')
            print(email[:index])
    elif action == 'replace':
        char = command[1]
        email = email.replace(char, '-')
        print(email)
    elif action == 'encrypt':
        for i in email:
            print(f'{"".join(str(ord(i)))}', end=' ')
