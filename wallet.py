class Wallet:
    def __init__(self, wallet_address, wallet_balance):
        self.__wallet_address = wallet_address
        self.__wallet_balance = wallet_balance

    def get_wallet_address(self):
        return self.__wallet_address
    
    def get_wallet_balance(self):
        return self.__wallet_balance

    def add_to_wallet(self, amount):
        self.__wallet_balance += amount

    def redeem_from_the_wallet(self, amount):
        if amount <= self.__wallet_balance:
            self.__wallet_balance -= amount
        else:
            print("Недостатньо коштів на рахунку")

    def display_wallet_info(self):
        print(f"Баланс гаманця: {self.__wallet_balance} USD")
