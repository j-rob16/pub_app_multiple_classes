class Customer:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def pay_for_drink(self, drink):
        self.wallet -= drink.price
