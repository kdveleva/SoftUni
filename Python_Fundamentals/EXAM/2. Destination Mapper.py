import re
pattern = r'(=|\/)([A-Z][A-Za-z]{2,})(=|\/)'

text = input()
points = 0
matches = []

find_iter = re.finditer(pattern, text)

for match in find_iter:
    if match.group(1) == match.group(3):
        matches.append(match.group(2))

print(f"Destinations: {', '.join(matches)}")
for i in matches:
    points += len(i)
print(f'Travel Points: {points}')

