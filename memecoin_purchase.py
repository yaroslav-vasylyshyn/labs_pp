from user import User
from wallet import Wallet
from order import Order

class MemeCoinPurchase(Order):
    def __init__(self, user, wallet, amount, coin_ticker):
        super().__init__(user, wallet, amount)
        self.coin_ticker = coin_ticker

    def confirm_purchase(self):
        if self.wallet.wallet_balance >= self.order_amount:
            print(f"Purchase {self.coin_ticker} for {self.user.user_name}")
            self.wallet.redeem_from_the_wallet(self.order_amount)
        else:
            print(f"Insuficient funds {self.coin_ticker}")

    def display_info(self):
        super().display_info()
        print(f"Куплений мемкоїн: {self.coin_ticker}")