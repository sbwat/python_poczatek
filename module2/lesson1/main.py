from shop.apple import Apples
from shop.potato import Potato
from shop.order import Order, OrderElement
from shop.product import Product
from shop.discounts import regular_discount, christmas_discount
from shop.data_generator import random_order_generator


def order_key(order):
    return order._total_order()


def class_example():
    red = Apples('red', 'big', 5)
    green = Apples('green', 'small', 3)
    old_potato = Potato("old", "small", 2)
    young_potato = Potato("young", "big", 10)
    print(repr(red))
    print(str(red))

    product1 = Product("Woda", "Jedzenie", 10)
    product2 = Product("wóda", "płyny", 20)
    product3 = Product("woda", "płyny", 10)
    print(product1 == product2)
    print(product1 == product3)
    print(product1 == red)

    oe1 = OrderElement(product1, 10)
    oe2 = OrderElement(product1, 5)
    oe3 = OrderElement(product2, 10)
    oe4 = oe1
    print(oe1 == oe2)
    print(oe1 == oe3)
    print(oe1 == oe4)
    print(str(oe1))

    ordered_products = random_order_generator(10)
    ordered_products2 = random_order_generator()

    print(ordered_products)
    print(ordered_products2)

    order3 = Order("Jacek",ordered_products)
    order4 = Order("Marek", ordered_products)
    order5 = Order("Jacek", ordered_products, discount=christmas_discount)
    order6 = Order("Adam", ordered_products, discount=regular_discount)

    print(str(order3))
    print(f"Długość zamówienia: {len(order3)}")
    order3.add_product(product1, 8)
    print(str(order3))
    print(f"Długość zamówienia: {len(order3)}")

    print(f"Porównanie 4 z 5: {order4 == order5}")
    print(f"Porównanie 4 z 6: {order4 == order6}")

    print(str(order4))
    print(str(order5))
    print(str(order6))



if __name__ == '__main__':
    class_example()
