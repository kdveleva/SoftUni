from collections import deque

queue = deque(input(). split(" "))
hot_potato = int(input())

while len(queue) > 1:
    queue.rotate(-hot_potato)
    loser = queue.pop()
    print(f'Removed {loser}')
winner = "".join(queue)
print(f'Last is {winner}')