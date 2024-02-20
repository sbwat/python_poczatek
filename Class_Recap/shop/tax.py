class TaxCalculator:
    FRUIT_VEGE_TAX = 5
    FOOD_TAX = 8
    OTHER_TAX = 20

    @staticmethod
    def tax(category, value):
        if category == "Owoce" or category == "Warzywa":
            return value * TaxCalculator.FRUIT_VEGE_TAX / 100
        elif category == "Jedzenie":
            return value * TaxCalculator.FOOD_TAX / 100
        else:
            return value * TaxCalculator.OTHER_TAX / 100
