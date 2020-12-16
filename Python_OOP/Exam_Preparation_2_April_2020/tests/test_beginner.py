import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):

    def setUp(self) -> None:
        self.beginner = Beginner("X")

    def test_name_empty_string(self):
        with self.assertRaises(ValueError):
            Beginner("")

    def test_damage_point_below_0(self):
        with self.assertRaises(ValueError):
            self.beginner.take_damage(-1)

    def test_health_point_below_0(self):
        with self.assertRaises(ValueError):
            self.beginner.health = -1

    def test_heath_will_decrease(self):
        self.beginner.take_damage(10)
        result = self.beginner.health
        self.assertEqual(result, 40)

    def test_is_not_dead(self):
        result = self.beginner.is_dead
        self.assertEqual(result, False)