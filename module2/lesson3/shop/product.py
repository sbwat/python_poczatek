class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"Nazwa: {self.name}, \t\t typ: {self.category}, \t\t cena: {self.price} zł/szt"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.name == other.name and self.category == other.category and self.price == other.price


class ProductExpire(Product):
    def __init__(self, name, category, price, production_year, expiration_time):
        super().__init__(name, category, price)
        self.production_year = production_year
        self.expiration_time = expiration_time

    def does_expire(self, current_year):
        return current_year - self.production_year > self.expiration_time

