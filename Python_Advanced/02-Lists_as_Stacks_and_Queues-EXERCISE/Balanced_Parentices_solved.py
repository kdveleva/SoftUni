from collections import deque

parenthesis = [x for x in input()]
parenthesis_2 = deque(parenthesis.copy())
balanced = True
par_pop = ''
par_append = []
r_sign = ''
for r in range(len(parenthesis)):
    par_pop = parenthesis_2.popleft()
    if par_pop in ["[", "{", "("]:
        par_append.append(par_pop)
    else:
        if len(par_append) == 0:
            print("NO")
            balanced = False
            break
        r_sign = par_append.pop()
        if par_pop == "}":
            if r_sign != "{":
                print("NO")
                balanced = False
                break
        elif par_pop == "]":
            if r_sign != "[":
                print("NO")
                balanced = False
                break
        elif par_pop == ")":
            if r_sign != "(":
                print("NO")
                balanced = False
                break

if balanced:
    print("YES")