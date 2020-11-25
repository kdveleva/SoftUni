from collections import defaultdict


def add_user(judge_dict):
    judge_dict[contest][username] = points


def total_points(points_dict):
    points_dict[username][contest] = points


judge = defaultdict(dict)
all_points = defaultdict(dict)
while True:
    command = input()
    if command == 'no more time':
        break
    command = command.split(' -> ')
    username, contest, points = command
    if contest in judge:
        if username in judge[contest]:
            if points < judge[contest][username]:
                continue
            else:
                add_user(judge)
                total_points(all_points)
        else:
            add_user(judge)
            total_points(all_points)
    else:
        add_user(judge)
        total_points(all_points)


for key, value in judge.items():
    print(f'{key}: {len(value)} participants')
    counter = 1
    for k, v in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f'{counter}. {k} <::> {v}')
        counter += 1

number = 1
print('Individual standings:')
p_sum = defaultdict(int)
for key, value in all_points.items():
    name = key
    total = sum(value.values())
    p_sum[name] = total

p_sum = dict(sorted(p_sum.items(), key=lambda x: (-x[1], x[0])))
for key, value in p_sum.items():
    print(f'{number}. {key} -> {value}')
    number += 1