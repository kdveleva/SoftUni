from project_Players_Monsters.hero import Hero
from project_Players_Monsters.elf import Elf

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
print(hero.__class__.__bases__[0].__name__)
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
muse_elf = Elf("ME", 2)
print(str(muse_elf))
print(muse_elf.__class__.__bases__[0].__name__)
print(muse_elf.username)
print(muse_elf.level)

# zero test
from project_Players_Monsters.hero import Hero
from project_Players_Monsters.elf import Elf
import unittest

class Tests(unittest.TestCase):
   def test(self):
      hero = Hero("H", 4)
      self.assertEqual(hero.username, "H")
      self.assertEqual(hero.level, 4)
      self.assertEqual(str(hero), "H of type Hero has level 4")
      elf = Elf("E", 4)
      self.assertEqual(str(elf), "E of type Elf has level 4")
      self.assertEqual(elf.__class__.__bases__[0].__name__, "Hero")
      self.assertEqual(elf.username, "E")
      self.assertEqual(elf.level, 4)

if __name__ == "__main__":
   unittest.main()