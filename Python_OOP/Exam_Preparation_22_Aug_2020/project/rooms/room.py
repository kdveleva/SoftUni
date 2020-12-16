class Room:
    family_name: str
    budget: float
    members_count: int
    children: list
    expenses: float

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value # NOTE: no exeception handling

    def calculate_expenses(self, *args):
        self.expenses = sum([el.get_monthly_expense() for el in args])
        # self.expenses = (el.cost for seq in args for el in seq)
        # total_cost = 0
        # for arg in args:
        #     total_cost += arg.cost
        # self.expenses = total_cost*30

    @property
    def cost(self):
        return self.expenses + self.room_cost

