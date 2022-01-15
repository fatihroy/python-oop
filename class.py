# inherritance

import csv #untuk csv
# mengambil data dari csv
# create class
class Item:
    pembayaran = 0.5 #pembayaran setelah diskon 50%
    product = []
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
        Item.product.append(self)

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
        # menampilkan secara otomatis dlm bentuk arraynya product
  # self.__class__.__name__ = fungsi untuk memanggil nama class untuk arraynya product
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity}) "
        

# membuat inherritance spy phone mewarisi class Item
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

       

phone1 = Phone("Han12x", 100, 5, 1)     
print(Item.product)
print(Phone.product)

