def factorial_division(a, b):
    a_sum = 1
    b_sum = 1
    for x in range(1, a+1):
        a_sum *= x
    for y in range(1, b+1):
        b_sum *= y
    a_sum_division_b_sum = a_sum / b_sum
    return f'{a_sum_division_b_sum:.2f}'


first_number = int(input())
second_number = int(input())

print(factorial_division(first_number, second_number))

