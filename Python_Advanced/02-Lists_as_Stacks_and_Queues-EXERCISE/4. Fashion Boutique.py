clothes = [int(x) for x in input().split(" ")]
rack_capacity = int(input())
removed_item = 0
shelf = []
counter = 0
returned = 0

while len(clothes) > 0:
    while sum(shelf) < rack_capacity and len(clothes) > 0:
        removed_item = clothes.pop()
        shelf.append(removed_item)
    counter += 1
    if sum(shelf) > rack_capacity:
        returned = shelf.pop()
        clothes.append(returned)
    shelf = []


print(counter)