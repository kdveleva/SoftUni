n = int(input())
word_dict = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in word_dict:
        word_dict[word] = []
    word_dict[word].append(synonym)

for word in word_dict:
    print(f'{word} - {", ".join(word_dict[word])}')