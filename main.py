from user import User
from wallet import Wallet
from order import Order
from memecoin_purchase import MemeCoinPurchase
from military_tax import MilitaryTax
from income_tax import IncomeTax
from totall_tax import TotalTax

def main():
    user1 = User("Ivan", "password123")
    wallet1 = Wallet("address1", 200)

    user2 = User("Olga", "securepass")
    wallet2 = Wallet("address2", 150)
    purchase1 = MemeCoinPurchase(user1, wallet1, 50, "RTD")
    purchase2 = MemeCoinPurchase(user2, wallet2, 80, "SHIB")

    print("\n--- Покупка мемкоїна ---")
    purchase1.confirm_purchase()
    purchase1.display_info()

    IncomeTax.display_income_tax_rate()
    MilitaryTax.display_military_tax_rate()

    tax1 = TotalTax(wallet1.wallet_balance)
    tax1.calculate_total_tax()

    print("\n--- Покупка мемкоїна ---")
    purchase2.confirm_purchase()
    purchase2.display_info()

    tax2 = TotalTax(wallet2.wallet_balance)
    tax2.calculate_total_tax()

    order1 = Order(user1, wallet1, 10)

    orders = [order1, purchase2]
    for order in orders:
        order.display_info()

main()