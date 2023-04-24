class Item:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def bought(self):
        self.quantity -= 1
