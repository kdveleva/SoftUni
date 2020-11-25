from collections import defaultdict
contests = defaultdict(str)
submissions = defaultdict(dict)
points_sum = defaultdict(int)
max_num = -999999999999999999
max_points = defaultdict(int)

while True:
    command = input()
    if command == "end of contests":
        break
    command = command.split(":")
    contest = command[0]
    password = command[1]
    contests[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    command = command.split('=>')
    contest_user = command[0]
    password_user = command[1]
    username = command[2]
    points = int(command[3])

    # Check if the contest is valid
    if contest_user not in contests.keys():
        continue

    # Check if the password is correct for the given contest
    if password_user not in contests[contest_user]:
        continue

    # Check if user in submissions
    if username not in submissions:
        submissions[username][contest_user] = points
    # Check if contest is new for the user
    elif contest_user not in submissions[username]:
        submissions[username][contest_user] = points
    # Check if points for contest are more than the old ones
    elif submissions[username][contest_user] < points:
        submissions[username][contest_user] = points

# Check which user has the most points
for key, value in submissions.items():
    points_sum[key] = sum(value.values())
user = ''
for key, value in points_sum.items():
    if value > max_num:
        max_num = value
        max_points[key] = max_num
        user = key
print(f"Best candidate is {user} with total {max_num} points.")

#After that print all students ordered by their names. For each user print each contest with the points in descending order
submissions = dict(sorted(submissions.items(), key=lambda x: (x[0])))
print("Ranking:")
for key, value in submissions.items():
    print(key)
    for v, i in sorted(value.items(), key=lambda x: -x[1]):
        print(f"#  {v} -> {i}")