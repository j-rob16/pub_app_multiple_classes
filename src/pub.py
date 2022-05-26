class Pub:
    
    def __init__(self, pub_name, till, drinks):
        self.name = pub_name
        self.till = till
        self.drinks = drinks

    def increase_till(self, cash):
        self.till += cash

    def sell_a_drink(self, drink):
        self.till += drink.price