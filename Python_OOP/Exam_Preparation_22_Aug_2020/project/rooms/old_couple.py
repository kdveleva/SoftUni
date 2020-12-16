from typing import List
from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):
    room_cost: int = 15
    appliances: list = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, budget=pension_one + pension_two, members_count=2)
        self.calculate_expenses(*self.appliances)
