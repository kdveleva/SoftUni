import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.card_repository = CardRepository()
        self.card = MagicCard("Gold")

    def test_if_card_is_already_added(self):
        with self.assertRaises(ValueError):
            self.card_repository.add(self.card)
            self.card_repository.add(self.card)

    def test_add_player(self):
        self.card_repository.add(self.card)
        result = len(self.card_repository.cards)
        self.assertEqual(result, 1)

    def test_add_count(self):
        self.card_repository.add(self.card)
        result = self.card_repository.count
        self.assertEqual(result, 1)

    def test_if_player_remove_is_empty_str(self):
        with self.assertRaises(ValueError):
            self.card_repository.remove("")

    def test_remove_player(self):
        self.card_repository.add(self.card)
        result = len(self.card_repository.cards)
        self.assertEqual(result, 1)
        self.card_repository.remove(self.card.name)
        result = len(self.card_repository.cards)
        self.assertEqual(result, 0)

    def test_remove_count(self):
        self.card_repository.add(self.card)
        result = self.card_repository.count
        self.assertEqual(result, 1)
        self.card_repository.remove(self.card.name)
        result = self.card_repository.count
        self.assertEqual(result, 0)

    def test_find_player(self):
        self.card_repository.add(self.card)
        result = self.card_repository.find(self.card.name)
        self.assertEqual(result, self.card)