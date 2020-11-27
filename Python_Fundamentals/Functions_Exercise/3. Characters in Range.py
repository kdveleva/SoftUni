def characters_in_between(char_a: str, char_b: str):
    list_characters = []
    for i in range(ord(char_a)+1, ord(char_b)):
        list_characters.append(chr(i))
    return list_characters


a = input()
b = input()


print(* characters_in_between(a, b))