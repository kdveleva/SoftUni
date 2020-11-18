from collections import deque
water_quantity = int(input())
queue = deque()
end = False

while True:
    if end:
        break
    command = input()
    if command == "Start":
        while True:
            litters_drunk = input().split()
            if litters_drunk[0] == "End":
                end = True
                break
            elif litters_drunk[0] == "refill":
                water_quantity += int(litters_drunk[1])
            elif int(litters_drunk[0]) <= water_quantity:
                print(f'{(queue.popleft())} got water')
                water_quantity -= int(litters_drunk[0])
            elif int(litters_drunk[0]) > water_quantity:
                print(f'{(queue.popleft())} must wait')

    queue.append(command)

print(f'{water_quantity} liters left')
