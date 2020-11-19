from typing import List
from project_Movie_world.customer import Customer
from project_Movie_world.dvd import DVD


class MovieWorld:

    name: str
    customers: List[Customer]
    dvds: List[DVD]

    _DVD_CAPACITY = 15
    _CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.customers_id = {}
        self.dvds = []
        self.dvd_id = {}

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
            self.customers_id[customer.id] = customer

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
            self.dvd_id[dvd.id] = dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.customers_id.get(customer_id)
        dvd = self.dvd_id.get(dvd_id)

        if customer.has_dvd(dvd):
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.add_dvd(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.customers_id.get(customer_id)
        dvd = self.dvd_id.get(dvd_id)

        if customer.has_dvd(dvd):
            customer.remove_dvd(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))
        return "\n".join(customers + dvds)
