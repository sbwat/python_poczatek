import random
from module1.lesson1.shop.product import Product, print_product


class Order():
    def __init__(self, name, shopping_list=None, total_price=0):
        self.name=name
        self.total_price=total_price
        self.list=shopping_list
        if shopping_list is None:
            shopping_list=[]
        self.total_price=total_order(shopping_list)
    def print_order(self):
        print("="*20)
        print(f"{self.name} zamówił/a: ")
        for prod in self.list:
            print_product(prod)
        print(f"Całkowita kwota zamówienia to: {self.total_price} zł.")
        print("="*20)
def total_order(shopping_list):
    total_price=0
    for i in shopping_list:
        total_price += i.price
    return total_price



def random_order_generator():
    new_list=[]
    size=random.randint(1,20)
    for i in range(size):
        prod_name="Produkt"+str(i)
        prod_cat="Kategoria"+str(random.randint(1,9))
        prod_price=random.randint(1,20)
        new_list.append(Product(prod_name,prod_cat,prod_price))
    return new_list