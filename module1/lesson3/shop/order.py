import random

from shop.product import Product


class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"{self.product}, \t Ilość: {self.quantity}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.quantity == other.quantity and self.product == other.product

    def total_price(self):
        return self.product.price * self.quantity


class Order:
    def __init__(self, name, shopping_list=None):
        self.name = name
        self._list = shopping_list
        if shopping_list is None:
            shopping_list = []
        self.total_price = self._total_order()

    def __str__(self):
        sepa = "=" * 40
        products = "\n"
        for prod in self._list:
            products += f"\t {prod}\n"
        return f"{sepa}\nZamawiający: {self.name}\nKwota całkowita zamówienia: {self._total_order()} zł.{products}\n{sepa}"

    def __len__(self):
        return len(self._list)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.name == other.name and len(self) == len(other):
            for product in self._list:
                if product not in other._list:
                    return False
            return True
        else:
            return False

    def _total_order(self):
        total_price = 0
        for i in self._list:
            total_price += OrderElement.total_price(i)
        return total_price

    def add_product(self, product, quantity):
        self._list.append(OrderElement(product, quantity))
        self.total_price = self._total_order()


def random_order_generator():
    new_list = []
    size = random.randint(1, 20)
    for i in range(size):
        prod_name = "Produkt" + str(i)
        prod_cat = "Kategoria" + str(random.randint(1, 9))
        prod_price = random.randint(1, 20)
        quantity = random.randint(1, 50)
        new_list.append(OrderElement(Product(prod_name, prod_cat, prod_price), quantity))
    return new_list
