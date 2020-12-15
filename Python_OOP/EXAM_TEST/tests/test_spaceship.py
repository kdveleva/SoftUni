import unittest

from project.spaceship.spaceship import Spaceship


class TestSpaceship(unittest.TestCase):

    def setUp(self) -> None:
        self.spaceship = Spaceship("Voyager", 1)

    def test_init(self):
        self.assertEqual(self.spaceship.name, "Voyager")
        self.assertEqual(self.spaceship.capacity, 1)
        self.assertEqual(self.spaceship.astronauts, [])

    def test_if_spaceship_full(self):
        with self.assertRaises(ValueError):
            self.spaceship.add("Gagarin")
            self.spaceship.add("Ivanov")

    def test_if_astronaut_is_already_in(self):
        with self.assertRaises(ValueError):
            self.spaceship.add("Gagarin")
            self.spaceship.add("Gagarin")

    def test_return_added_astronaut(self):
        result = self.spaceship.add("Gagarin")
        self.assertEqual(result, "Added astronaut Gagarin")

    def test_if_name_not_in_astronauts(self):
        with self.assertRaises(ValueError):
            self.spaceship.remove("Gagarin")

    def test_return_remove(self):
        result = self.spaceship.add("Gagarin")
        result = self.spaceship.remove("Gagarin")
        self.assertEqual(result, "Removed Gagarin")


if __name__ == "__main__":
    unittest.main()
