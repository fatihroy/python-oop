# import Item
from Item import Item


class Phone(Item):
    
    def __init__(self, name:str, price:float, quantity=0, broken=0):
        # pemanggilan ke super function untuk bisa akses semua attribut dari Item
        super().__init__(
          name, price, quantity
        )
       
        
        # membuat aturan value bahwa price & quantity harus >=0
        assert broken >= 0, f"{quantity} is not equal to or greater than 0"

        # meng-assingn object
        self.broken = broken
