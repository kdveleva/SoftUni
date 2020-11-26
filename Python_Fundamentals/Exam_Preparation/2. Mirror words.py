import re

text = input()
pattern = r'#([a-z]{3,})##([a-z]{3,})#|@([a-z]{3,})@@([a-z]{3,})@'

counter = 0

matches = re.finditer(pattern, text, re.IGNORECASE)
m_list = []

for match in matches:
    counter += 1
    if '#' in match.group(0):
        if match.group(1) == match.group(2)[::-1]:
            m_list.append(f'{match.group(1)} <=> {match.group(2)}')
    elif "@" in match.group(0):
        if match.group(3) == match.group(4)[::-1]:
            m_list.append(f'{match.group(3)} <=> {match.group(4)}')


if counter > 0:
    print(f'{counter} word pairs found!')
else:
    print('No word pairs found!')
if len(m_list) > 0:
    print('The mirror words are:')
    print(', '.join(m_list))
else:
    print('No mirror words!')

