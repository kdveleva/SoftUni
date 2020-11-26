import re

pattern = r'(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([\D\W]{3})<(.+)'

n = int(input())

for _ in range(n):
    password = input()
    matches = re.finditer(pattern, password)
    pr = re.findall(pattern, password)

    for match in matches:
        if match.group(1) == match.group(6):
            if '<' not in match.group(5) and '>' not in match.group(5):
                print(f'Password: {"".join(match.group(2, 3, 4, 5))}')
            else:
                print('Try another password!')
        else:
            print('Try another password!')

    if len(pr) == 0:
        print('Try another password!')