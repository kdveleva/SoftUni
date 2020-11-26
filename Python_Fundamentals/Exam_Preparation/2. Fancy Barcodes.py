import re
pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'
n = int(input())
group = '00'
valid = False
for _ in range(n):
    valid = False
    text = input()
    matches = re.finditer(pattern,text)
    for match in matches:
        for l in match.group(1):
            if l.isdigit():
                if group == '00':
                    group = ''
                group += l
        valid = True
        print(f"Product group: {group}")
        group = '00'

    if not valid:
        print('Invalid barcode')