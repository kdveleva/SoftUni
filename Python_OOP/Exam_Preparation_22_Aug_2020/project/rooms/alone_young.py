from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    room_cost: int = 10
    appliances: list = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, members_count=1)
        self.calculate_expenses(*self.appliances)

