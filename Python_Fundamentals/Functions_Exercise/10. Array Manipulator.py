import sys


def exchange(array, index):
    return array[index + 1:] + array[:index + 1]


def max_odd_even(array, index):
    global divider_result
    max_num = -sys.maxsize
    max_place = []
    if index == 'even':
        divider_result = 0
    elif index == 'odd':
        divider_result = 1
    for i, n in enumerate(array):
        if n % 2 == divider_result and n >= max_num:
            max_num = n
            max_place.append(i)
    return max_place[-1:]


def min_odd_even(array, index):
    global divider_result
    min_num = sys.maxsize
    min_place = []
    if index == 'even':
        divider_result = 0
    elif index == 'odd':
        divider_result = 1
    for i, n in enumerate(array):
        if n % 2 == divider_result and n <= min_num:
            min_num = n
            min_place.append(i)
    return min_place[-1:]


def first_odd_even(array, index_1, index_2):
    global divider_result
    first_list = []
    counter = 0
    if index_2 == 'even':
        divider_result = 0
    elif index_2 == 'odd':
        divider_result = 1
    for i in array:
        if counter == index_1:
            break
        if i % 2 == divider_result:
            first_list.append(i)
            counter += 1
    return first_list


def last_odd_even(array, index_1, index_2):
    global divider_result
    last_list = []
    counter = 0
    if index_2 == 'even':
        divider_result = 0
    elif index_2 == 'odd':
        divider_result = 1
    for i in reversed(array):
        if counter == index_1:
            break
        if i % 2 == divider_result:
            counter += 1
            last_list.append(i)
        last_list.reverse()
    return last_list


array_input = input().split(' ')
array_int = map(int, array_input)
array_int = list(array_int)
all_new_arrays = []

while True:
    command = input().split(' ')
    if command[0] == 'end':
        break

    if command[0] == 'exchange':
        index = int(command[1])
        if len(array_input) <= index or index < 0:
            all_new_arrays.append('Invalid index')
        else:
            array_int = exchange(array_int, index)

    elif command[0] == 'max':
        index_1 = command[1]
        result = max_odd_even(array_int, index_1)
        if len(result) == 0:
            all_new_arrays.append('No matches')
        else:
            all_new_arrays.append(*result)

    elif command[0] == 'min':
        index_1 = command[1]
        result = min_odd_even(array_int, index_1)
        if len(result) == 0:
            all_new_arrays.append('No matches')
        else:
            all_new_arrays.append(*result)

    elif command[0] == 'first':
        index_1 = int(command[1])
        index_2 = command[2]
        if len(array_int) < index_1:
            all_new_arrays.append('Invalid count')
        else:
            result = first_odd_even(array_int, index_1, index_2)
            all_new_arrays.append(result)

    elif command[0] == 'last':
        index_1 = int(command[1])
        index_2 = command[2]
        if len(array_int) < index_1:
            all_new_arrays.append('Invalid count')
        else:
            result = last_odd_even(array_int, index_1, index_2)
            all_new_arrays.append(result)

for i in all_new_arrays:
    print(i)
print(array_int)
