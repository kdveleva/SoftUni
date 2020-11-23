from collections import deque
parenthesis = deque([x for x in input()])
char = ''
char_2 = ''
char_3 = ''
check = []

balanced = True

while len(parenthesis):
    char = parenthesis.popleft()
    check.append(char)
    for c in range(len(parenthesis)):
        char_2 = parenthesis.popleft()
        check.append(char_2)
        if check == ["{", "}"]: #or check == ["}", "{"]:
            check.clear()
            break
        elif check == ["[", "]"]: #or check == ["]", "["]:
            check.clear()
            break
        elif check == ["(", ")"]: #or check == [")", "("]:
            check.clear()
            break
        char_3 = check.pop()
        parenthesis.append(char_3)
