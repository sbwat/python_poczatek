class Product():
    def __init__(self,name,category,price):
        self.name=name
        self.category=category
        self.price=price
    def print_product(self):
        print(f"Nazwa: {self.name},\t typ: {self.category},\t cena: {self.price} zł.")