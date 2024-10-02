class IncomeTax:
    RATE = 0.18

    def __init__(self, income: float):
        if income < 0:
            raise ValueError("Дохід не може бути від'ємним.")
        self.income = income  

    @staticmethod
    def display_income_tax_rate():
        print(f"Податок на прибуток в Україні станом на 2024 рік становить: {IncomeTax.RATE * 100}%")

    def calculate_income_tax(self) -> float:
        return self.income * IncomeTax.RATE

    def display_tax_info(self):
        tax = self.calculate_income_tax()
        print(f"Дохід: {self.income} USD, Податок на прибуток: {tax} USD")
