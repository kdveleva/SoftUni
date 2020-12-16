import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):

    def setUp(self) -> None:
        self.trap_card = TrapCard("Silver")

    def test_if_string_is_empty(self):
        with self.assertRaises(ValueError):
            TrapCard("")

    def test_if_damage_points_are_below_zero(self):
        with self.assertRaises(ValueError):
            self.trap_card.damage_points = -1

    def test_if_health_points_are_below_zero(self):
        with self.assertRaises(ValueError):
            self.trap_card.health_points = -1