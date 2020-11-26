import re
n = int(input())
pattern = r'U\$([A-Z][a-z]{2,})U\$P@\$([a-zA-Z]{5,}[0-9]+)P@\$'
counter = 0
for _ in range(n):
    text = input()
    matches = re.findall(pattern, text)
    if len(matches) > 0:
        counter += 1
        print('Registration was successful')
        print(f'Username: {matches[0][0]}, Password: {matches[0][1]}')
    else:
        print(f'Invalid username or password')

print(f'Successful registrations: {counter}')