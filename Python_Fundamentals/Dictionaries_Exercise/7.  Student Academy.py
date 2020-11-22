from collections import defaultdict

rows = int(input())
academy = {}
for i in range(rows):
    name = input()
    grade = float(input())
    if name not in academy:
        academy[name] = []
    academy[name].append(grade)

sort_by_grade = {k: sum(v) / len(v) for k, v in academy.items() if (sum(v) / len(v)) > 4.49}
# for k, v in academy.items():
#     average = sum(v) / len(v)
#     if average > 4.49:
#         sort_by_grade[k] = average

sort_by_name = dict(sorted(sort_by_grade.items(), key=lambda x: x[1], reverse=True))

for k, v in sort_by_name.items():
    print(f'{k} -> {v:.2f}')
