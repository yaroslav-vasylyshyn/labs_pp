class Wallet:
    def __init__(self, wallet_address, wallet_balance):
        self.__wallet_address = wallet_address
        self.__wallet_balance = wallet_balance

    @property
    def wallet_address(self):
        return self.__wallet_address
    
    @property
    def wallet_balance(self):
        return self.__wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, amount):
        if amount >= 0:
            self.__wallet_balance = amount
        else:
            print("Сума повинна бути більше або дорівнювати 0")

    def redeem_from_the_wallet(self, amount):
        if amount <= self.__wallet_balance:
            self.__wallet_balance -= amount
        else:
            print("Недостатньо коштів на рахунку")

    def display_wallet_info(self):
        print(f"Баланс гаманця: {self.__wallet_balance} USD")
