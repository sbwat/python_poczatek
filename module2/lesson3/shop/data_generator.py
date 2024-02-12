import random
from shop.order import OrderElement, Order
from shop.product import Product

MIN_PRICE = 1
MAX_PRICE = 20

MIN_QUANTITY = 1
MAX_QUANTITY = 50

def random_order_generator(size=None):
    if size is None:
        size = random.randint(1, Order.MAX_ORDER_ELEMENTS)
    new_list = []
    for i in range(size):
        prod_name = "Produkt" + str(i)
        prod_cat = "Kategoria" + str(random.randint(1, 9))
        prod_price = random.randint(MIN_PRICE, MAX_PRICE)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        new_list.append(OrderElement(Product(prod_name, prod_cat, prod_price), quantity))

    return new_list
