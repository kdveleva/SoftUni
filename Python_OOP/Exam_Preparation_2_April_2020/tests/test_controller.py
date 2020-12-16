import unittest

from project.controller import Controller


class TestController(unittest.TestCase):

    def setUp(self) -> None:
        self.controller = Controller()

    def test_if_beginner_is_added(self):
        self.controller.add_player("Beginner", "Beginner")
        result = len(self.controller.player_repository.players)
        self.assertEqual(result, 1)

    def test_if_advanced_is_added(self):
        self.controller.add_player("Advanced", "Advanced")
        result = len(self.controller.player_repository.players)
        self.assertEqual(result, 1)

    def test_custom_str_beginner_advanced_add_player(self):
        result = self.controller.add_player("Beginner", "Beginner")
        self.assertEqual(result, "Successfully added player of type Beginner with username: Beginner")
        result = self.controller.add_player("Advanced", "Advanced")
        self.assertEqual(result, "Successfully added player of type Advanced with username: Advanced")

    def test_if_card_is_added(self):
        self.controller.add_card("Magic", "Magic")
        result = len(self.controller.card_repository.cards)
        self.assertEqual(result, 1)
        self.controller.add_card("Trap", "Trap")
        result2 = len(self.controller.card_repository.cards)
        self.assertEqual(result2, 2)

    def test_custom_string_add_card(self):
        result = self.controller.add_card("Magic", "Magic")
        self.assertEqual(result, "Successfully added card of type MagicCard with name: Magic")
        result = self.controller.add_card("Trap", "Trap")
        self.assertEqual(result, "Successfully added card of type TrapCard with name: Trap")

    def test_if_card_is_added_to_players_deck(self):
        self.controller.add_player("Beginner", "Beginner")
        self.controller.add_card("Magic", "Magic")
        result = self.controller.add_player_card("Beginner", "Magic")
        self.assertEqual(result, "Successfully added card: Magic to user: Beginner")
        player = self.controller.player_repository.find("Beginner")
        result = len(player.card_repository.cards)
        self.assertEqual(result, 1)

    def test_fight_cut_string(self):
        self.controller.add_player("Beginner", "Beginner")
        self.controller.add_card("Magic", "Magic")
        self.controller.add_player_card("Beginner", "Magic")
        self.controller.add_player("Advanced", "Advanced")
        self.controller.add_card("Magic", "Silver")
        self.controller.add_player_card("Advanced", "Silver")
        result = self.controller.fight("Beginner", "Advanced")
        self.assertEqual(result, "Attack user health 165 - Enemy user health 295")

    def test_report(self):
        self.controller.add_player("Beginner", "Beginner")
        self.controller.add_card("Magic", "Magic")
        self.controller.add_player_card("Beginner", "Magic")
        self.controller.add_player("Advanced", "Advanced")
        self.controller.add_card("Magic", "Silver")
        self.controller.add_player_card("Advanced", "Silver")
        result = self.controller.report()
        self.assertEqual(result, """Username: Beginner - Health: 50 - Cards 1
### Card: Magic - Damage: 5
Username: Advanced - Health: 250 - Cards 1
### Card: Silver - Damage: 5
""")

