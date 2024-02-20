class Apple:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def __repr__(self):
        return f"Nazwa: {self.name}, wielkość: {self.size}, cena: {self.price} zł/kg."
