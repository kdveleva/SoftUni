import re
text = input()
pattern = r'::([A-Z][a-z]{2,})::|\*\*([A-Z][a-z]{2,})\*\*'
matches = re.finditer(pattern, text)
cool = 1
emogi = 0
cool_emogi = []
total = []

for m in text:
    if m.isdigit():
        cool *= int(m)

for i in matches:
    total.append(i.group(0))
    if "::" in i.group(0):
        for w in i.group(1):
            emogi += ord(w)
    elif "**" in i.group(0):
        for w in i.group(2):
            emogi += ord(w)
    if emogi >= cool:
        cool_emogi.append(i.group(0))
    emogi = 0

print(f'Cool threshold: {cool}')
print(f'{len(total)} emojis found in the text. The cool ones are:')
for x in range(len(cool_emogi)):
    print(f'{"".join(cool_emogi[x])}')
