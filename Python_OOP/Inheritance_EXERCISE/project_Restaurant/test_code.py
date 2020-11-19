from project_Restaurant.beverage.beverage import Beverage
from project_Restaurant.beverage.coffee import Coffee
from project_Restaurant.beverage.tea import Tea
from project_Restaurant.food.soup import Soup
from project_Restaurant.product import *

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
print(product.price)

late = Coffee("late", 458)
print(late.name)
tea = Tea("coco", 10, 10)
print(tea.__class__.__bases__[0].__name__)
