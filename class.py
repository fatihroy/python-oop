# create class
class Item:
    pembayaran = 0.5 #pembayaran setelah diskon 50%
    # init akan di kerjakan otomatis ketika classnya dipanggil
                   #mengubah tipe data | nilai default
    def __init__(self, name:str, price:float, quantity=0):
        print(f"The name is :{name}")
        # membuat aturan value bahwa price & quantity harus >=0
        assert price >= 0, f"{price} is not equal to or greater than 0" #menambah pesan kesalahan
        assert quantity >= 0, f"{quantity} is not equal to or greater than 0"
        # meng-assingn object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self): #ini adalah method
        return self.price*self.quantity #gak perlu parameters karena sudah tau

    def diskon(self):
        # self.price = self.price * Item.pembayaran (dikali denagn Item.pembayaran)
        self.price = self.price * self.pembayaran # (dikali denagn self.pembayaran)
item1 = Item('book', 5)
# item1.name = "book" bisa didelete krn sudah dideklarasikan di self.name
# item1.price = 10
# item1.quantity = 5
item1.diskon()
print(item1.price)

item2 = Item('pen', 10, 100) 
item2.pembayaran = 0.2 #membuat pembayaran sendiri untuk item2
item2.diskon()
print(item2.price)
# print(Item.__dict__) #menunjukkan seluruh atribut di Item
# print(item1.__dict__) #menunjukkan seluruh atribut di item1
# print(item2.__dict__) #menunjukkan seluruh atribut di item2
# print(Item.pembayaran)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
