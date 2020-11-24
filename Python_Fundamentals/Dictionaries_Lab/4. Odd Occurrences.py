words = input().lower().split(' ')
dictionary = {}
count = 1
odd_occurrences = []

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = count

for key, value in dictionary.items():
    if value % 2 != 0:
        odd_occurrences.append(key)

print(* odd_occurrences)