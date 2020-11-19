from project_Movie_world.dvd import DVD


class Customer:
    name: str
    age: int
    id: int
    rented_dvds: list

    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def has_dvd(self, dvd: DVD):
        return dvd in self.rented_dvds

    def add_dvd(self, dvd: DVD):
        self.rented_dvds.append(dvd)

    def remove_dvd(self, dvd: DVD):
        self.rented_dvds.remove(dvd)

    def __repr__(self):
        rented_dvd = ', '.join(x.name for x in self.rented_dvds)
        return str(f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's"
                   f" ({rented_dvd})")