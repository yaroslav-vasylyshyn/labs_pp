from user import User
from wallet import Wallet

class Order:
    def __init__(self, user, wallet, order_amount):
        self.user = user 
        self.wallet = wallet  
        self.order_amount = order_amount

    def confirm_order(self):
        print(f"Підтвердження замовлення для {self.user.user_name} на суму {self.order_amount} USD")
        self.wallet.redeem_from_the_wallet(self.order_amount)

    def display_info(self):
        self.user.display_user_info()
        print(f"Сума замовлення: {self.order_amount} USD")
        print(f"Баланс після замовлення: {self.wallet.wallet_balance} USD")
