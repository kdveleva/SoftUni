def lenght(password):
    if len(password) < 6 or len(password_input) > 10:
        return 'Password must be between 6 and 10 characters'


def character(password):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return 'Password must consist only of letters and digits'


def digit(password):
    counter = 0
    for dig in password:
        if dig.isdigit():
            counter += 1
    if counter < 2:
        return 'Password must have at least 2 digits'


def valid(password):
    validators = [
        lenght,
        character,
        digit
    ]
    errors = []
    for validator in validators:
        result = validator(password)
        if result is not None:
            errors.append(result)
    if len(errors) == 0:
        return 'Password is valid'
    else:
        return '\n'.join(errors)


password_input = input()
print(valid(password_input))