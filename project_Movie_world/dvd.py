import calendar


class DVD:
    name: str
    id: int
    creation_year: int
    creation_month: str
    age_restriction: int
    is_rented: bool

    def __init__(
            self, name: str, id: int, creation_year: int,
            creation_month: str, age_restriction: int
    ):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        _, month, year = date.split(".")
        name_month = calendar.month_name[int(month)]
        return cls(name, id, int(year), name_month, age_restriction)

    def __repr__(self):
        rented_status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} " \
               f"{self.creation_year}) has age restriction {self.age_restriction}. " \
               f"Status: {rented_status}"