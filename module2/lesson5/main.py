from shop.apple import Apples
from shop.potato import Potato
from shop.order import Order, OrderElement, ExpressOrder
from shop.product import Product, ProductExpire
from shop.discounts import PercentageDiscount, AbsoluteDiscount
from shop.data_generator import random_order_generator


def order_key(order):
    return order._total_order()

def apply_discount(discount_type, order_value, discount_value):
    return discount_type.apply_discount(order_value, discount_value)


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
    twenty_perc_discount = PercentageDiscount(discount_percentage=20)
    hundred_pln_discount = AbsoluteDiscount(discount_value=100)

    order3 = Order("Jacek",ordered_products)
    order4 = Order("Marek", ordered_products)
    order5 = Order("Jacek", ordered_products, discount=twenty_perc_discount)
    order6 = Order("Adam", ordered_products, discount=hundred_pln_discount)

    print(str(order3))
    print(f"Długość zamówienia: {len(order3)}")
    order3.add_product(product1, 8)
    print(str(order3))
    print(f"Długość zamówienia: {len(order3)}")

    print(f"Porównanie 4 z 5: {order4 == order4}")
    print(f"Porównanie 4 z 6: {order4 == order6}")

    print(str(order4))
    print(str(order5))
    print(str(order6))

    for elements in order4.list:
        print(elements)

    order4.list = ordered_products2
    print(order4)
    print(order4.total_price)

    productexp1 = ProductExpire("Woda", "Jedzenie", 10, 2020, 5)
    productexp2 = ProductExpire("wóda", "płyny", 20, 2000, 10)
    print(f"{productexp1.name} jest już po terminie przydatności -> {productexp1.does_expire(2024)}")
    print(f"{productexp2.name} jest już po terminie przydatności -> {productexp2.does_expire(2024)}")

    express_order = ExpressOrder("Marek", "15-02-2024", random_order_generator())
    print(express_order)

if __name__ == '__main__':
    class_example()
