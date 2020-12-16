from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.people.child import Child


class YoungCoupleWithChildren (Room):
    room_cost: int = 30
    appliances: list = []
    children: list = [Child]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children: Child):
        members_count = len(children) + 2
        super().__init__(family_name, budget=salary_one + salary_two, members_count=members_count)
        self.children = list(children)
        for _ in range(len(children)+2):
            self.appliances.append(Laptop())
            self.appliances.append(Fridge())
            self.appliances.append(TV())
        self.calculate_expenses(*self.appliances, *self.children) # there is an issue here

