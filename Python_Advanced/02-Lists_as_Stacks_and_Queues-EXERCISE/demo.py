from collections import deque


def calculate_time(time_in_seconds):  # returns timestamp
    time_in_seconds %= 86400  # reset time to 24 h
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    timestamp = f"{hours:0>2d}:{minutes:0>2d}:{seconds:0>2d}"
    return timestamp


robots_raw = input().split(";")
robots = {}  # dict {robot: time, ...}
for robot in robots_raw:  # store all robots and their production time:
    name, time = robot.split("-")
    robots[name] = int(time)

hours, minutes, seconds = list(map(int, input().split(":")))
time = (hours * 3600) + (minutes * 60) + seconds  # convert time to seconds

products = deque()  # deque of products
while True:  # fetch products
    command = input()
    if command == "End":
        break
    else:
        product = command
        products.append(product)

robot_availability = robots.copy()  # copy of robots
while products:  # this is our production line
    time += 1  # add one second
    product = products.popleft()  # fetch current product

    for robot in robot_availability:  # check if robot IS NOT AVAILABLE, and adds a second to its current production time if NOT
         if robot_availability[robot] < robots[robot]:
            robot_availability[robot] += 1

    for robot in robot_availability: # checks if robot IS AVAILABLE, sets production time to 0 if YES (robot is now busy!), prints, breaks
        if robot_availability[robot] == robots[robot]:
            robot_availability[robot] = 0
            print(f"{robot} - {product} [{calculate_time(time)}]")
            break
    else:
        products.append(product)  # if no robot available, enqueue product at the end of queue