from project.factory.factory import Factory


class ChocolateFactory(Factory):
    recipes: dict  # recipe name as key and dictionary of needed ingredients to make the recipe
    products: dict  # recipe name as key and quantity as value

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        if ingredient_type not in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {__class__.__name__}")
        if ingredient_type not in self.ingredients:
            self.ingredients[ingredient_type] = quantity
        else:
            self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError("No such product in the factory")
        if self.ingredients[ingredient_type] - quantity < 0:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes.keys():
            raise TypeError("No such recipe")
        if recipe_name not in self.products:
            self.products[recipe_name] = 1 # what should be the quantity
        else:
            self.products[recipe_name] += 1
            for name, recipe in self.recipes.items():
                if name == recipe_name:
                    for ingredient, quantity in recipe.items():
                        self.remove_ingredient(ingredient, quantity)
        return self.products
