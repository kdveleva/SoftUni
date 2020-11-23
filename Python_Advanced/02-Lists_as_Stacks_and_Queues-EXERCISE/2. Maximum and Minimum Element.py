n = int(input())
stack = []
for _ in range(n):
    commands = input().split(" ")
    command = commands[0]
    if command == '1':
        stack.append(int(commands[1]))
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command == '4':
        if stack:
            print(min(stack))

ordered = [str(x) for x in reversed(stack)]
print(f"{', '.join(ordered)}")