import csv #untuk csv
# mengambil data dari csv
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

    @classmethod
    def ambil_dariCSV(cls):
        with open('item.csv', 'r') as L: #ambil dari item.csv 
            reader = csv.DictReader(L) #supaya data di item.csv terbaca
            items = list(reader) #dijadikan list

        # tampilkan satu persatu
        for item in items:
          
            Item(
                # mengambil nama, harga, kuantitas
                name = item.get('nama'),
                # mengubah jadi int krn semua yang ada di csv adalah string
                price = float(item.get('harga')),
                quantity = int(item.get('kuantitas')),
            )

    def __repr__(self):
        # menampilkan secara otomatis dlm bentuk arraynya produk
        return f"item('{self.name}',{self.price},{self.quantity}) "
        
    


Item.ambil_dariCSV()
print(Item.produk)