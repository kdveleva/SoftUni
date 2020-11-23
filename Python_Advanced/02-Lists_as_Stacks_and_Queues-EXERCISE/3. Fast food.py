from collections import deque

quantity_of_the_food = int(input())
queue = deque([int(x) for x in input().split(' ')])
print(max(queue))
order = 0

while quantity_of_the_food > 0:
    if queue:
        if queue[0] > quantity_of_the_food:
            print(f"Orders left: {' '.join([str(x) for x in queue])}")
            break
        order = queue.popleft()
        quantity_of_the_food -= order
    else:
        break


if len(queue) == 0:
    print("Orders complete")