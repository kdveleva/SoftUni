import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):

    def setUp(self) -> None:
        self.magic_card = MagicCard("Gold")

    def test_if_string_is_empty(self):
        with self.assertRaises(ValueError):
            MagicCard("")

    def test_if_damage_points_are_below_zero(self):
        with self.assertRaises(ValueError):
            self.magic_card.damage_points = -1

    def test_if_health_points_are_below_zero(self):
        with self.assertRaises(ValueError):
            self.magic_card.health_points = -1
