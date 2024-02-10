import random
from module1.lesson1.shop.product import Product

class OrderElement():
    def __init__(self,product,quantity):
        self.product=product
        self.quantity=quantity

    def total_price(self):
        return self.product.price*self.quantity

    def print(self):
        print(f"Nazwa: {self.product.name},\t Typ: {self.product.category}, \t Cena/kg [zł]: {self.product.price},"
              f"\t Ilość [kg]: {self.quantity}, \t Cena [zł]: {self.total_price()}")

class Order():
    def __init__(self, name, shopping_list=None, total_price=0):
        self.name=name
        self.total_price=total_price
        self.list=shopping_list
        if shopping_list is None:
            shopping_list=[]
    def print_order(self):
        print("="*20)
        print(f"{self.name} zamówił/a: ")
        for prod in self.list:
            OrderElement.print(prod)
        print(f"Całkowita kwota zamówienia to: {self.total_order()} zł.")
        print("="*20)
    def total_order(self):
        total_price=0
        for i in self.list:
            total_price += OrderElement.total_price(i)
        return total_price

def random_order_generator():
    new_list=[]
    size=random.randint(1,20)
    for i in range(size):
        prod_name="Produkt"+str(i)
        prod_cat="Kategoria"+str(random.randint(1,9))
        prod_price=random.randint(1,20)
        quantity=random.randint(1,50)
        new_list.append(OrderElement(Product(prod_name,prod_cat,prod_price),quantity))
    return new_list