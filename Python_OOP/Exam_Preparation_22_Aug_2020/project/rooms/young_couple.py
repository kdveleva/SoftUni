from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple (Room):
    room_cost: int = 20
    appliances: list = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2)
        self.calculate_expenses(*self.appliances)
