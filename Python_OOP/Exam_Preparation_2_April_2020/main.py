# from project.player.advanced import Advanced
# from project.player.beginner import Beginner
# from project.player.player_repository import PlayerRepository
# import unittest
#
# b = Beginner("X")
# c = Advanced("Y")
# repo = PlayerRepository()
# print(repo.add(b))
# repo.add(b)
# print(repo.add(c))
# print(repo.remove("X"))




# player_1 = Beginner("X")
# player_2 = Beginner("Y")
#
# magic = MagicCard("Magic")
# trap = TrapCard("Trap")
#
# player_1.card_repository.add(magic)
# player_1.card_repository.add(trap)
#
# player_2.card_repository.add(magic)
# player_2.card_repository.add(trap)
#
#
# fight = BattleField()
# print(fight.fight(player_1, player_2))
from project.controller import Controller

control = Controller()
print(control.add_player("Beginner", "X"))
print(control.add_player("Advanced", "Y"))

print(control.add_card("Magic", "Gold",))
print(control.add_card("Trap", "Silver"))
#
print(control.add_player_card("X", "Gold"))

print(control.add_player_card("X", "Silver"))

print(control.add_player_card("Y", "Gold"))
print(control.add_player_card("Y", "Silver"))
#
print(control.fight("X", "Y"))
#
print(control.report())
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
