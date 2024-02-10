from apple import Apples
from potato import Potato
from shop.order import Order, print_order, random_order_generator
# from shop.product import Product, print_product


def class_example():
    red = Apples('red','big',5)
    green = Apples('green','small',3)
    old_potato = Potato("old","small",2)
    young_potato = Potato("young","big", 10)


    print(f"Typ {red} to {type(red)}")
    print(f"Typ {green} to {type(green)}")
    print(f"Typ {old_potato} to {type(old_potato)}")
    print(f"Typ {young_potato} to {type(young_potato)}")

    # order1 = Order("Jacek",[red, green])
    #
    # products = {
    #     "Jabłko": Product('jabłko', 'owoce', 5),
    #     "Ziemniak": Product('ziemniak','warzywa',2),
    #     "Marchewka": Product('marchew','warzywa',3)
    # }
    # print(products)
    #
    # order2=Order("Kasia",[products["Ziemniak"],products["Marchewka"],products["Jabłko"]])
    # print_product(products['Jabłko'])
    # print_order(order2)
    order3=Order("Jacek",random_order_generator())
    print_order(order3)


if __name__ == '__main__':
    class_example()