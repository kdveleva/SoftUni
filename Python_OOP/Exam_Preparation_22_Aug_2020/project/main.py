from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren

from project.people.child import Child

from project.everland import Everland

everland = Everland()


def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child_one = Child(5, 1, 2, 1)
    child_two = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


# Room("a", 2, 3)
# Appliance(1)
# Fridge()
# TV()
# Laptop()
# Stove()
# Child(1, 2, 3)
# AloneOld('a', 1)
# AloneYoung('a', 1)
# OldCouple('a', 1, 2)
# YoungCouple('a', 1, 2)
# YoungCoupleWithChildren('a', 1, 2)

if __name__ == "__main__":
    test_one()
