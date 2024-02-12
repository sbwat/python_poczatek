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

    # def print_product(self):
    #     print(f"Nazwa: {self.name},\t typ: {self.category},\t cena: {self.price} zł.")
