class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"Nazwa: {self.name}, kategoria: {self.category}, cena/kg: {self.price} zł"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.name == other.name and self.category == other.category and self.price == other.price

class ProductWithExpirationDate(Product):

    def __init__(self,name, category, price, production_date, expiration_date):
        super().__init__(name, category, price)
        self.production_date = production_date
        self.expiration_date = expiration_date

    def does_expire(self, current_year):
        return current_year-self.production_date > self.expiration_date


