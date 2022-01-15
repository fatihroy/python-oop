from Item import Item

class Phone(Item):

    def __init__(self, name, price, quantity, broken=0):
        super().__init__(
            name, price, quantity
        )
        self.broken = broken
    
    @classmethod
    def harga_total(self):
        self.price = (self.quantity - self.broken) * Item.diskon

