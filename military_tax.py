class MilitaryTax:
    RATE = 0.015
    def __init__(self, income):
        self.income = income  

    @staticmethod
    def display_military_tax_rate():
        print(f"Військовий збір в Україні станом на 2024 рік становить: {MilitaryTax.RATE * 100}%")

    def calculate_military_tax(self) -> float:
        """Розрахунок військового збору."""
        return self.income * MilitaryTax.RATE