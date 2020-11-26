import re

pattern = r'\|([A-Z]{4,})\|:#([a-zA-Z]+\s[a-zA-Z]+)#'

n = int(input())
for _ in range(n):
    lines = input()
    matches = re.findall(pattern, lines)
    if len(matches) == 0:
        print('Access denied!')
        continue
    for i in matches:
        print(", The ".join(i))
    print(f'>> Strength: {len(matches[0][0])}')
    print(f'>> Armour: {len(matches[0][1])}')
