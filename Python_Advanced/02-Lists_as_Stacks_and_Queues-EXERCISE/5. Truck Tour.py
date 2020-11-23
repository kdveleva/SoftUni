from collections import deque
n = int(input())
pumps = deque()
fuel = 0

for _ in range(n):
    pump = [int(x) for x in input().split(' ')]
    pumps.append(pump)

for i in range(n):
    current = pumps[i]
    fuel = 0
    while pumps:
        fuel += current[0]
        if fuel >= current[1]:
            current = pumps.popleft()
            fuel -= current[1]
        else:
            pumps.append(current)
            break
    if not pumps:
        print(i)
        break
