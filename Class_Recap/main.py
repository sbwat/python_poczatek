from shop.data_generator import generate_order
from shop.discounts import AbsoluteDiscount, PercentageDiscount
from shop.order import Order


def shop_example():
    fifty_percent = PercentageDiscount(50)
    hundred_pln = AbsoluteDiscount(100)
    shopping_list = generate_order(size=10)

    order_nodisc = Order("Jan", "Kowalski", shopping_list)
    print(order_nodisc)
    order_perc = Order("Jan", "Kowalski", shopping_list, fifty_percent)
    print(order_perc)
    order_abso = Order("Jan", "Kowalski", shopping_list, hundred_pln)
    print(order_abso)



if __name__ == "__main__":
    shop_example()
