def sum_numbers(a, b):
    return a + b


def subtract(c):
    return c


input_a = int(input())
input_b = int(input())
input_c = int(input())


def add_and_subtract():
    return sum_numbers(input_a, input_b) - subtract(input_c)


print(add_and_subtract())
