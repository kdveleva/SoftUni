from abc import ABC, abstractmethod


class Factory(ABC):
    name: str
    capacity: int # should be for one product or for all products
    ingredients: dict  # name of the ingredient
                       # for key and quantity of
                       # the ingredient as a value

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        ...

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        ...

    def can_add(self, value: int): # this could be for one or more
        if self.capacity >= sum(self.ingredients.values())+value:
            return value

