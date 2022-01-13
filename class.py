# create class
class Item:
    pembayaran = 0.5 #pembayaran setelah diskon 50%
    produk = []
    # init akan di kerjakan otomatis ketika classnya dipanggil
                   #mengubah tipe data | nilai default
    def __init__(self, name:str, price:float, quantity=0):
        # membuat aturan value bahwa price & quantity harus >=0
        assert price >= 0, f"{price} is not equal to or greater than 0" #menambah pesan kesalahan
        assert quantity >= 0, f"{quantity} is not equal to or greater than 0"
        # meng-assingn object
        self.name = name
        self.price = price
        self.quantity = quantity
        # menambahkan item
        Item.produk.append(self)

    def calculate_total_price(self): #ini adalah method
        return self.price*self.quantity #gak perlu parameters karena sudah tau

    def diskon(self):
        # self.price = self.price * Item.pembayaran (dikali denagn Item.pembayaran)
        self.price = self.price * self.pembayaran # (dikali denagn self.pembayaran)

    def __repr__(self):
        # menampilkan secara otomatis dlm bentuk arraynya produk
        return f"item('{self.name}',{self.price},{self.quantity}) "
        
item1 = Item('Letter', 10, 100)
item2 = Item('Hvs', 5, 100)
item3 = Item('Bag', 7, 100)
item4 = Item('Pen', 10, 100)
item5 = Item('book', 1, 10)

# menampilkan item1-item5 satu-satu
# for i in Item.produk:
#     print(i.name)
print(Item.produk)