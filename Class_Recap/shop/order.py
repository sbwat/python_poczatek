import random

from shop.product import Product
from shop.tax import TaxCalculator
from shop.discounts import DiscountPolicy

class Order:
    REGULAR_CUSTOMER_DISCOUNT = 5
    CHRISTMAS_DISCOUNT = 20
    MAX_ORDER_ELEMENTS = 15

    def __init__(self, first_name, last_name, product_list=None, discount_policy = None):
        if product_list is None:
            self._list = []
        self._list = product_list
        self.name = first_name + " " + last_name
        if discount_policy is None:
            self.discount = DiscountPolicy()
        else:
            self.discount = discount_policy


    def __str__(self):
        products = ""
        sep = 40 * "="
        for order_element in self._list:
            products += f"{order_element}, podatek: {order_element.tax} zł \n"
        return (f"{sep} \nZamawiający: {self.name} \n\n{products}"
                f"Wartość całkowita zamówienia: {self.total_price} zł. \n {sep}")

    def __len__(self):
        return len(self._list)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.name == other.name and len(self) == len(other):
            for element in self._list:
                if element not in other._list:
                    return False
            return True
        else:
            return False

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self,value):
        if len(value) <= Order.MAX_ORDER_ELEMENTS:
            self._list = value
        else:
            self._list = value[:Order.MAX_ORDER_ELEMENTS]


    @property
    def total_price(self):
        total_price = 0
        for product in self._list:
            total_price += product.total_price

        return self.discount.apply_discount(total_price)


    def add_product(self, product, amount):
        new_post = OrderElement(product,amount)
        if len(self._list) < Order.MAX_ORDER_ELEMENTS:
            self._list.append(new_post)
        else:
            print("Osiągnięto maksymalną ilość elementów zamówienia.")


class ExpressOrder(Order):
    EXPRESS_ORDER_CHARGE = 20
    def __init__(self,first_name, last_name, delivery_date, product_list=None, discount_policy = None):
        super().__init__(first_name, last_name, product_list, discount_policy)
        self.delivery = delivery_date
    def __str__(self):
        products = ""
        sep = 40 * "="
        for order_element in self._list:
            products += f"{order_element}, podatek: {order_element.tax} zł \n"
        return (f"{sep} \nZamawiający: {self.name} \t Data dostawy: {self.delivery} \n\n{products}"
                f"Wartość zamówienia: {self.total_price} zł. \n {sep}")

    @property
    def total_price(self):
        return super().total_price + ExpressOrder.EXPRESS_ORDER_CHARGE



class OrderElement:
    def __init__(self, product, ammount):
        self.product = product
        self.ammount = ammount
        self.total_price = self.product.price*self.ammount
        self.tax = TaxCalculator.tax(self.product.category,self.total_price)

    def __str__(self):
        return f" {self.product}, ilość: {self.ammount}, łącznie: {self.total_price} zł"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.ammount == other.ammount





