import random

from shop.product import Product
from shop.order import OrderElement, Order

MAX_PRICE = 50

MIN_PRICE = 1

MIN_ORDER_SIZE = 1

MAX_ORDER_SIZE = 20


def generate_order(first_name=None, last_name=None, size=None, discount=None):
    if first_name is None:
        first_name = "Anonymous"
    if last_name is None:
        last_name = "User"
    if size is None:
        size = random.randint(MIN_ORDER_SIZE, MAX_ORDER_SIZE)
    shopping_list = []
    for _ in range(size):
        name = "Produkt_" + str(_)
        category = "Inne"
        price = random.randint(MIN_PRICE, MAX_PRICE)
        shopping_list.append(OrderElement(Product(name, category, price), random.randint(1, 10)))
    return shopping_list
