class Item:
    pembayaran = 0.5
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

  
    def diskon(self):
     self.price = self.price * self.pembayaran
     return self.price 