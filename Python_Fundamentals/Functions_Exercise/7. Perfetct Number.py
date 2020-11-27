def perfect_number(number):
    positive_sum = 0
    for i in range(1, number):
        if number % i == 0:
            positive_sum += i
    if positive_sum == number:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


number_input = int(input())
print(perfect_number(number_input))