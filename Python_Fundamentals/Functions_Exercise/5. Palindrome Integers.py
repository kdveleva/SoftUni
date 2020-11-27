def palindrome_integers(a: str):
    a = a.split(', ')
    reversed_i = ''
    normal_i = ''
    palindrome = None
    result = []
    for i in a:
        reversed_i = reversed(i)
        normal_i = i
        if list(reversed_i) == list(normal_i):
            palindrome = True
        else:
            palindrome = False
        result.append(str(palindrome))
    return '\n'.join(result)


a_input = input()

print(palindrome_integers(a_input))
