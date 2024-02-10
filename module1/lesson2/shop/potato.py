class Potato():
    def __init__(self, type, size, price,weight,total=0):
        self.type = type
        self.size = size
        self.price = price
        self.weight=weight
        self.total=self.total_price()


    def total_price(self):
        return self.price*self.weight