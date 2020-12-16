from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    player_repository: PlayerRepository
    card_repository: CardRepository

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type_p: str, username: str):
        if type_p == "Beginner":
            self.player_repository.add(Beginner(username))
        elif type_p == "Advanced":
            self.player_repository.add(Advanced(username))
        return f"Successfully added player of type {type_p} with username: {username}"

    def add_card(self, type_c: str, name: str):
        if type_c == "Magic":
            self.card_repository.add(MagicCard(name))
        elif type_c == "Trap":
            self.card_repository.add(TrapCard(name))
        return f"Successfully added card of type {type_c}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        card_to_add = self.card_repository.find(card_name)
        player = self.player_repository.find(username)
        player.card_repository.add(card_to_add)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField().fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        s = ""
        for player in self.player_repository.players:
            s += f"Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}\n"
            for card in player.card_repository.cards:
                s += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return s

#
# control = Controller()
# print(control.add_player("Beginner", "X"))
# print(control.add_player("Advanced", "Y"))
#
# print(control.add_card("Magic", "Gold",))
# print(control.add_card("Magic", "Silver"))
#
# #
# print(control.add_player_card("X", "Gold"))
#
#
#
#
# print(control.add_player_card("Y", "Silver"))
# #
# print(control.fight("X", "Y"))
# # #
# print(control.report())