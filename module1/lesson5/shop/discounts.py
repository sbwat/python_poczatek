REGULAR_DISCOUNT = 5
CHRISTMAS_DISCOUNT = 20


def no_discount(price):
    return price


def regular_discount(price):
    return price*(100-REGULAR_DISCOUNT)/100


def christmas_discount(price):
    if price > 100:
        return price-CHRISTMAS_DISCOUNT
    return price
