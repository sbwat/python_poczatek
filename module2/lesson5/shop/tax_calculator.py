class Tax:
    FRUIT_VEGE_TAX = 0.05
    FOOD_TAX = 0.08
    OTHER_TAX = 0.2

    def __init__(self, category, value):
        self.category = category
        self.value = value

    @staticmethod
    def calculate(category, value):
        if category == "Owoce" or category == "Warzywa":
            tax_val = value * Tax.FRUIT_VEGE_TAX
        elif category == "Jedzenie":
            tax_val = value * Tax.FOOD_TAX
        else:
            tax_val = value * Tax.OTHER_TAX
        return tax_val
