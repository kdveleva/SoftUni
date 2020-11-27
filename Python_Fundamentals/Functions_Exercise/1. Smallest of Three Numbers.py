def smallest_number(a, b, c):
    min_num = 999999999999
    if a < min_num:
        min_num = a
    if b < min_num:
        min_num = b
    if c < min_num:
        min_num = c
    return min_num


input_a = int(input())
input_b = int(input())
input_c = int(input())

print(smallest_number(input_a, input_b, input_c))
