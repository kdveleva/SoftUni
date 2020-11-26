n = int(input())
heroes_dict = {}
for _ in range(n):
    text = input(). split(' ')
    hero_name, HP, MP = text
    if hero_name not in heroes_dict:
        heroes_dict[hero_name] = []
    if int(HP) > 100:
        HP = 100
    if int(MP) > 200:
        MP = 100
    heroes_dict[hero_name].append(int(HP))
    heroes_dict[hero_name].append(int(MP))


while True:
    command = input().split(' - ')
    action = command[0]
    if action == "End":
        break
    elif action == "CastSpell": # MP
        cast, hero_name, mp_needed, spell_name = command
        if hero_name not in heroes_dict:
            continue
        if heroes_dict[hero_name][1] >= int(mp_needed) and heroes_dict[hero_name][1] >= 0:
            heroes_dict[hero_name][1] -= int(mp_needed)
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage": # HP
        take_damage, hero_name, damage, attacker = command
        if hero_name not in heroes_dict:
            continue
        heroes_dict[hero_name][0] -= int(damage)
        if heroes_dict[hero_name][0] <= 0:
            heroes_dict.pop(hero_name)
            print(f'{hero_name} has been killed by {attacker}!')
        else:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")

    elif action == "Recharge": # MP
        recharge, hero_name, amount = command
        if hero_name not in heroes_dict:
            continue
        heroes_dict[hero_name][1] += int(amount)
        if heroes_dict[hero_name][1] > 199:
            recovered = abs((heroes_dict[hero_name][1] - 200) - int(amount))
            print(f"{hero_name} recharged for {recovered} MP!")
            heroes_dict[hero_name][1] = 200
        else:
            print(f"{hero_name} recharged for {amount} MP!")

    elif action == "Heal": # HP
        heal, hero_name, amount = command
        if hero_name not in heroes_dict:
            continue
        heroes_dict[hero_name][0] += int(amount)
        if heroes_dict[hero_name][0] > 99:
            recovered = abs((heroes_dict[hero_name][0] - 100) - int(amount))
            print(f"{hero_name} healed for {recovered} HP!")
            heroes_dict[hero_name][0] = 100
        else:
            print(f"{hero_name} healed for {amount} HP!")

heroes_dict = dict(sorted(heroes_dict.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in heroes_dict.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
