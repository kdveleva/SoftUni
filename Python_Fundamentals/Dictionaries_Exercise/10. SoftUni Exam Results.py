from collections import defaultdict

results = defaultdict(int)
submissions = defaultdict(list)

while True:
    commands = input()
    if commands == "exam finished":
        break
    if "banned" in commands:
        command = commands.split('-')
        results.pop(command[0])
        continue
    command = commands.split('-')
    username = command[0]
    language = command[1]
    points = int(command[2])

    submissions[language].append(username)

    if username in results:
        if results[username] > points:
            continue
        else:
            results[username] = points
    else:
        results[username] = points

results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
submissions = dict(sorted(submissions.items(), key=lambda x: (-len(x[1]), x[0])))

print("Results:")
for k, v in results.items():
    print(f'{k} | {v}')
print('Submissions:')
for k, v in submissions.items():
    print(f'{k} - {len(v)}')