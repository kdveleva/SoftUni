

def sum_of_numbers(a: str):
    even_sum = 0
    odd_sum = 0
    for i in a:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        elif i % 2 == 1:
            odd_sum += i
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


a_input = input()

print(sum_of_numbers(a_input))
