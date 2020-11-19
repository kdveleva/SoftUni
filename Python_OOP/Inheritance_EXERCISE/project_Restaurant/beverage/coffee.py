from typing import ClassVar
from .hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS: ClassVar[int] = 50
    COFFEE_PRICE: ClassVar[float] = 3.50
    __caffeine: float

    def __init__(self, name, caffeine):
        super().__init__(name, Coffee.COFFEE_PRICE, Coffee.COFFEE_MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, var):
        self.__caffeine = var
