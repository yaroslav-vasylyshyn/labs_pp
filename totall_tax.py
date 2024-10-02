from income_tax import IncomeTax
from military_tax import MilitaryTax

class TotalTax(IncomeTax, MilitaryTax):
    def __init__(self, income: float):
        IncomeTax.__init__(self, income)  
        MilitaryTax.__init__(self, income) 

    def calculate_total_tax(self) -> float:
        total_tax = self.calculate_income_tax() + self.calculate_military_tax()
        print(f"Загальний податок: {total_tax}")
        return total_tax  