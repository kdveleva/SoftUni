from project.rooms.room import Room


class Everland:
    rooms: list

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        # Calculate the expenses of each room + the room_cost
        total_consumption = sum([r.cost for r in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        # If the budget of the family is enough to pay for the month
        s = ''
        room_to_delete = []
        for room in self.rooms:
            if room.budget >= room.cost:
                room.budget -= room.cost
                s += f"{room.family_name} paid {room.cost:.2f}$ and " \
                     f"have {room.budget:.2f}$ left.\n"
            else:
                room_to_delete.append(room)
                s += f"{room.family_name} does not have enough budget and must leave the hotel."
        for room_del in room_to_delete:
            self.rooms.pop(self.rooms.index(room_del))
        return s

    def status(self):
        s = ''
        # Return information about the hotel. If there are children in the room, print them first, and then the appliances monthly cost.
        all_people_in_the_hotel = sum([x.members_count for x in self.rooms])
        child_cost = 0
        s += f"Total population: {all_people_in_the_hotel}\n"
        for room in self.rooms:
            s += f"{room.family_name} with {room.members_count} members. " \
                 f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            for n, child in enumerate(room.children, 1):
                s += f"--- Child {n} monthly cost: {child.get_monthly_expense():.2f}$\n"
                child_cost += child.cost * 30
            s += f"--- Appliances monthly cost: {room.expenses - child_cost:.2f}$\n"
        return s
