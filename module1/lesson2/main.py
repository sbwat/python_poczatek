from shop.apple import Apples
from shop.potato import Potato
from shop.order import Order, OrderElement ,random_order_generator
from shop.product import Product

def class_example():
    red = Apples('red','big',5)
    green = Apples('green','small',3)
    old_potato = Potato("old","small",2)
    young_potato = Potato("young","big", 10)

    print(red.total_price(5))
    # print(f"Typ {red} to {type(red)}")
    # print(f"Typ {green} to {type(green)}")
    # print(f"Typ {old_potato} to {type(old_potato)}")
    # print(f"Typ {young_potato} to {type(young_potato)}")

    order3=Order("Marek",random_order_generator())
    order3.print_order()

if __name__ == '__main__':
    class_example()