import random
from shop.product import Product
from shop.tax_calculator import Tax


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
    MAX_ORDER_ELEMENTS = 20

    def __init__(self, name, shopping_list=None):
        self.name = name
        if shopping_list is None:
            shopping_list = []
        if len(shopping_list) > Order.MAX_ORDER_ELEMENTS:
            self._list = shopping_list[:Order.MAX_ORDER_ELEMENTS]
        else:
            self._list = shopping_list
        self.total_price = self._total_order()

    def __str__(self):
        total_tax = 0
        sepa = "=" * 40
        products = "\n"
        for prod in self._list:
            tax = Tax.calculate(prod.product.category, prod.total_price())
            products += f"\t {prod} \t\t Podatek: {tax: .2f} zł.\n"
            total_tax += tax
        return (f"{sepa}\nZamawiający: {self.name}\nKwota całkowita zamówienia: {self._total_order()} zł.{products}\n"
                f"Podatek do zapłacenia: {total_tax: .2f} zł. \n"
                f"Całkowita kwota do zapłaty: {self._total_order()+total_tax: .2f} zł. \n{sepa}")

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
        if len(self._list) >= Order.MAX_ORDER_ELEMENTS:
            print(f"Przekroczono limit produktów, nowy produkt nie został dodany!")
        else:
            self._list.append(OrderElement(product, quantity))
            self.total_price = self._total_order()

    @classmethod
    def random_order_generator(cls, name):
        new_list = []
        size = random.randint(1, cls.MAX_ORDER_ELEMENTS)
        for i in range(size):
            prod_name = "Produkt" + str(i)
            prod_cat = "Kategoria" + str(random.randint(1, 9))
            prod_price = random.randint(1, 20)
            quantity = random.randint(1, 50)
            new_list.append(OrderElement(Product(prod_name, prod_cat, prod_price), quantity))

        order = Order(name, new_list)
        return order
