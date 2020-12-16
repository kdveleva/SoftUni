import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hw = Hardware("HDD", 'Power', 200, 200)

    def test_set_attr(self):
        self.assertEqual(self.hw.name, 'HDD')
        self.assertEqual(self.hw.type, 'Power')
        self.assertEqual(self.hw.capacity, 200)
        self.assertEqual(self.hw.memory, 200)
        self.assertEqual(len(self.hw.software_components), 0)

    def test_install_raises(self):
        with self.assertRaises(Exception) as ex:
            sw = Software('Desktop', 'Light', 3000, 1000)
            self.hw.install(sw)
        self.assertEqual(str(ex.exception), "Software cannot be installed")

    def test_install_sw(self):
        sw = Software('Desktop', 'Light', 100, 100)
        self.hw.install(sw)
        self.assertEqual(self.hw.software_components, [sw])

    def test_uninstall_sw(self):
        sw = Software('Desktop', 'Light', 100, 100)
        self.hw.install(sw)
        self.hw.uninstall(sw)
        self.assertEqual(len(self.hw.software_components), 0)


if __name__ == '__main__':
    unittest.main()