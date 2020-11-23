from collections import deque


def convert_time_sec(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds


def convert_time_hours(time):
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    return hour, minutes, seconds


robots = {x.split("-")[0]: int(y)
          for x in input().split(";")
          for y in x.split("-") if y.isdigit()}

time = [int(x) for x in input().split(":")]
hours, minutes, seconds = time[0], time[1], time[2]
converted_sec = (convert_time_sec(hours, minutes, seconds))
total_seconds_worked = 0


materials = deque()

while True:
    command = input()
    if command == "End":
        break
    materials.append(command)


for key in robots.keys():
    material = materials.popleft()
    total_seconds_worked += 1
    converted_sec += 1
    h, m, s = convert_time_hours(converted_sec)
    print(f"{key} - {material} "
          f"[{h:02d}:{m:02d}:{s:02d}]")
worked = False
total_seconds_with_element = 0
while len(materials):
    material = materials.popleft()
    for key, value in robots.items():
        if value != total_seconds_with_element:
            worked = False
        else:
            worked = True
            converted_sec += total_seconds_with_element
            h, m, s = convert_time_hours(converted_sec)
            print(f"{key} - {material} "
                  f"[{h:02d}:{m:02d}:{s:02d}]")
            total_seconds_with_element = 0
            break
    if not worked:
        materials.append(material)
    total_seconds_with_element += 1