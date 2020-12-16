import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):

    def setUp(self) -> None:
        self.advanced = Advanced("X")

    def test_name_empty_string(self):
        with self.assertRaises(ValueError):
            Advanced("")

    def test_damage_point_below_0(self):
        with self.assertRaises(ValueError):
            self.advanced.take_damage(-1)

    def test_health_point_below_0(self):
        with self.assertRaises(ValueError):
            self.advanced.health = -1

    def test_heath_will_decrease(self):
        self.advanced.take_damage(50)
        result = self.advanced.health
        self.assertEqual(result, 200)

    def test_is_not_dead(self):
       result = self.advanced.is_dead
       self.assertEqual(result, False)

    def test_take_damage(self):
        self.assertEqual(self.advanced.health, 250)
        self.advanced.take_damage(50)
        self.assertEqual(self.advanced.health, 200)


