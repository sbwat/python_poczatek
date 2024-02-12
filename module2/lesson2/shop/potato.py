class Potato:
    def __init__(self, type, size, price):
        self.type = type
        self.size = size
        self.price = price

    def __repr__(self):
        return f"<Potato type='{self.type}', size='{self.size}', price='{self.price}'>"

    def total_price(self, weight):
        return self.price * weight
