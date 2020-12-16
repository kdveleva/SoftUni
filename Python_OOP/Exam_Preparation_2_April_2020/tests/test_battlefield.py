import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattlefield(unittest.TestCase):

    def setUp(self) -> None:
        self.battlefield = BattleField()
        self.player_beginner = Beginner("Beginner")
        self.player_advanced = Advanced("Advanced")
        self.card_magic = MagicCard("Magic")
        self.card_trap = TrapCard("Trap")

    def test_if_player_is_dead(self):
        with self.assertRaises(ValueError):
            self.player_advanced.health = 0
            self.battlefield.fight(self.player_advanced, self.player_beginner)

    def test_if_health_is_added_to_beginner(self):
        self.battlefield.fight(self.player_advanced, self.player_beginner)
        result = self.player_beginner.health
        self.assertEqual(result, 90)
        result = self.player_advanced.health
        self.assertEqual(result, 250)

    def test_if_damage_is_added_to_cards(self):
        magic_card_2 = MagicCard("Magic_2")
        self.player_advanced.card_repository.cards.append(self.card_magic)
        self.player_beginner.card_repository.cards.append(magic_card_2)
        self.battlefield.fight(self.player_advanced, self.player_beginner)
        result = sum([c.damage_points for c in self.player_advanced.card_repository.cards])
        self.assertEqual(result, 5)
        result = sum([c.damage_points for c in self.player_beginner.card_repository.cards])
        self.assertEqual(result, 35)

    def test_if_sum_card_points_are_added_to_player_health(self):
        magic_card_2 = MagicCard("Magic_2")
        self.player_advanced.card_repository.cards.append(self.card_magic)
        self.player_beginner.card_repository.cards.append(magic_card_2)
        self.battlefield.fight(self.player_advanced, self.player_beginner)
        result = self.player_advanced.health
        self.assertEqual(result, 295)
        result = self.player_beginner.health
        self.assertEqual(result, 165)
