from shop.tax_calculator import Tax
from shop.discounts import DiscountPolicy


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

    def __init__(self, name, shopping_list=None, discount=None):
        self.name = name
        if shopping_list is None:
            shopping_list = []
        if len(shopping_list) > Order.MAX_ORDER_ELEMENTS:
            self._list = shopping_list[:Order.MAX_ORDER_ELEMENTS]
        else:
            self._list = shopping_list

        if discount is None:
            discount = DiscountPolicy()
        self.discount = discount

    def __str__(self):
        total_tax = 0
        sepa = "=" * 40
        products = "\n"
        for prod in self._list:
            tax = Tax.calculate(prod.product.category, prod.total_price())
            products += f"\t {prod} \t\t Podatek: {tax: .2f} zł.\n"
            total_tax += tax
        return (f"{sepa}\nZamawiający: {self.name}\nKwota całkowita zamówienia: {self.total_price} zł.{products}\n"
                f"Podatek do zapłacenia: {total_tax: .2f} zł. \n"
                f"Całkowita kwota do zapłaty: {self.total_price+total_tax: .2f} zł. \n{sepa}")

    def __len__(self):
        return len(self._list)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.name == other.name and len(self) == len(other):
            for product in self._list:
                if product not in other.list:
                    return False
            return True
        else:
            return False

    @property
    def list(self):
        return self._list

    @property
    def total_price(self):
        total_price = 0
        for i in self._list:
            total_price += OrderElement.total_price(i)
        return self.discount.apply_policy(total_price)


    @list.setter
    def list(self, value):
        if len(value) < Order.MAX_ORDER_ELEMENTS:
            self._list = value
        else:
            self._list = value[:Order.MAX_ORDER_ELEMENTS]


    def add_product(self, product, quantity):
        if len(self._list) >= Order.MAX_ORDER_ELEMENTS:
            print(f"Przekroczono limit produktów, nowy produkt nie został dodany!")
        else:
            self._list.append(OrderElement(product, quantity))

class ExpressOrder(Order):

    EXPRESS_ORDER_CHARGE = 15
    def __init__(self, name, delivery_date, shopping_list=None, discount=None):
        super().__init__(name, shopping_list, discount)
        self.delivery_date = str(delivery_date)

    def __str__(self):
        total_tax = 0
        sepa = "=" * 40
        products = "\n"
        for prod in self._list:
            tax = Tax.calculate(prod.product.category, prod.total_price())
            products += f"\t {prod} \t\t Podatek: {tax: .2f} zł.\n"
            total_tax += tax
        return (f"{sepa}\nZamawiający: {self.name}\nPrzewidywana data dostawy: {self.delivery_date}\n"
                f"Kwota całkowita zamówienia: {self.total_price} zł.{products}\n"
                f"Podatek do zapłacenia: {total_tax: .2f} zł. \n"
                f"Całkowita kwota do zapłaty: {self.total_price+total_tax: .2f} zł. \n{sepa}")

    @property
    def total_price(self):
        total_price = 0
        for i in self._list:
            total_price += OrderElement.total_price(i)
        return self.discount.apply_policy(total_price) + self.EXPRESS_ORDER_CHARGE
