from collections import defaultdict
miner_dict = defaultdict(int)

while True:
    resources = input()
    if resources == "stop":
        break
    quantity = int(input())
    miner_dict[resources] += quantity

for key, value in miner_dict.items():
    print(f'{key} -> {value}')