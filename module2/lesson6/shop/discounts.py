class DiscountPolicy:
    def apply_policy(self, order_value):
        return order_value


class PercentageDiscount(DiscountPolicy):

    def __init__(self, discount_percentage):
        self.discount = discount_percentage

    def apply_policy(self, order_value):
        return order_value*(100-self.discount)/100


class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, discount_value):
        self.discount = discount_value

    def apply_policy(self, order_value):
        if order_value < self.discount:
            return 0
        return order_value - self.discount
