from typing import ClassVar
from .dessert import Dessert


class Cake(Dessert):

    CAKE_PRICE: ClassVar[float] = 5
    CAKE_GRAMS: ClassVar[float] = 250
    CAKE_CALORIES: ClassVar[float] = 1000

    def __init__(self, name):
        super().__init__(name, self.__class__.CAKE_PRICE, self.__class__.CAKE_GRAMS, self.__class__.CAKE_CALORIES)

