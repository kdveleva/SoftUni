from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    name: str
    chocolate_factory: ChocolateFactory
    egg_factory: EggFactory
    paint_factory: PaintFactory
    storage: dict

    def __init__(self, name, chocolate_factory, egg_factory, paint_factory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}  # product name as key and quantity of the product as value

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        chocolate = self.chocolate_factory.make_chocolate(recipe)
        for k, v in chocolate.items():
            self.storage[k] = v

    def paint_egg(self, color: str, egg_type: str):
        if egg_type not in self.egg_factory.ingredients or color not in self.paint_factory.ingredients:
            raise ValueError("Invalid commands")
        if f"{color} {egg_type}" not in self.storage:
            self.storage[f"{color} {egg_type}"] = 1
        else:
            self.storage[f"{color} {egg_type}"] += 1
        self.egg_factory.remove_ingredient(egg_type, 1)
        self.paint_factory.remove_ingredient(color, 1)

    def __repr__(self):
        s = f"Shop name: {self.name}\n"
        s += "Shop Storage:\n"
        for k, v in self.storage.items():
            s += f"{k}: {v}\n"
        return s



#
#
# cf = ChocolateFactory("Choco", 100)
# ef = EggFactory("Egg", 100)
# pf = PaintFactory("Paint", 100)
#
#
# shop = EasterShop("shop", cf, ef, pf)
# shop.add_chocolate_ingredient("milk chocolate", 50)
# shop.add_chocolate_ingredient("sugar", 50)
# shop.chocolate_factory.add_recipe("hot cocoa", {"milk chocolate": 10})
# shop.chocolate_factory.add_recipe("cold cocoa", {"milk chocolate": 10, "sugar": 10})
# shop.add_egg_ingredient("chicken egg", 10)
# shop.add_paint_ingredient("blue", 10)
# shop.make_chocolate("hot cocoa")
# shop.make_chocolate("hot cocoa")
# shop.make_chocolate("hot cocoa")
# shop.make_chocolate("cold cocoa")
# shop.make_chocolate("cold cocoa")
#
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# shop.paint_egg("blue", "chicken egg")
# print(shop)

