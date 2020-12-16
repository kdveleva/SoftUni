from project.rooms.room import Room


class AloneOld(Room):
    room_cost: int = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, members_count=1)


