courses_dict = {}
while True:
    command = input()
    if command == 'end':
        break
    tokens = command.split(' : ')
    course = tokens[0]
    student = tokens[1]
    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(student)

sort_dict = dict(sorted(courses_dict.items(), key=lambda c: len(c[1]), reverse=True))

for key, value in sort_dict.items():
    print(f'{key}: {len(value)}')
    for item in sorted(value):
        print(f'-- {item}')
