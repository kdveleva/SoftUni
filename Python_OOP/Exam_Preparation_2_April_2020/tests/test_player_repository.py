import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.player_repository = PlayerRepository()
        self.player = Beginner("Test")

    def test_if_player_is_already_added(self):
        with self.assertRaises(ValueError):
            self.player_repository.add(self.player)
            self.player_repository.add(self.player)

    def test_add_player(self):
        self.player_repository.add(self.player)
        result = len(self.player_repository.players)
        self.assertEqual(result, 1)

    def test_add_count(self):
        self.player_repository.add(self.player)
        result = self.player_repository.count
        self.assertEqual(result, 1)

    def test_if_player_remove_is_empty_str(self):
        with self.assertRaises(ValueError):
            self.player_repository.remove("")

    def test_remove_player(self):
        self.player_repository.add(self.player)
        result = len(self.player_repository.players)
        self.assertEqual(result, 1)
        self.player_repository.remove(self.player.username)
        result = len(self.player_repository.players)
        self.assertEqual(result, 0)

    def test_remove_count(self):
        self.player_repository.add(self.player)
        result = self.player_repository.count
        self.assertEqual(result, 1)
        self.player_repository.remove(self.player.username)
        result = self.player_repository.count
        self.assertEqual(result, 0)

    def test_find_player(self):
        self.player_repository.add(self.player)
        result = self.player_repository.find(self.player.username)
        self.assertEqual(result, self.player)
