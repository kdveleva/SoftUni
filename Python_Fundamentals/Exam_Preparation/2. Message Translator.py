import re

pattern = r'!([A-Z][a-z]{2,})!:\[([a-zA-Z]{8,})\]'
act = ''
n = int(input())
encryption = []
for _ in range(n):
    text = input()
    matches = re.finditer(pattern, text)
    for m in matches:
        for i in m.group(2):
            i = ord(i)
            encryption.append(i)
            act = m.group(1)
    if len(encryption) == 0:
        print(f'\nThe message is invalid')
    else:
        print(f'{act}:', end=' ')
        for i in encryption:
            print(f'{"".join(str(i))}', end=" ")
    encryption = []
