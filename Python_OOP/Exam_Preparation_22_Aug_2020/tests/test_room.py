import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):

    def test_init(self):
        room = Room('name', 1000, 3)
        for attr in ['family_name', 'budget', 'members_count', 'children', 'expenses']:
            self.assertTrue(hasattr(room, attr))

        self.assertEqual(room.family_name, 'name')
        self.assertEqual(room.budget, 1000.00)
        self.assertEqual(room.members_count, 3)
        self.assertEqual(room.children, [])
        self.assertEqual(room.expenses, 0)

    def test_exception(self):
        with self.assertRaises(ValueError) as ve:
            Room('a', 1, 1).expenses = - 5
        self.assertEqual(str(ve.exception), "Expenses cannot be negative")


