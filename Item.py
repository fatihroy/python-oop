# Getters and Setters

import csv
from logging import exception #untuk csv
# mengambil data dari csv

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
        # self.name = name tidak boleh seperti ini karena ada property
        self.__name = name
        self.__price= price
        self.quantity = quantity
        
        # menambahkan item
        Item.product.append(self)

    def new_method(self):
        self.price
    
    @property
    def price(self):
        return self.__price
        
    @property
    # property decorator = Hanya Membaca di atribut
    def name(self): #supaya kalau ketik self.name maka hasilnya adalah self.name dan tidak bisa diubah
        print('anda mencoba mendapatkan name')
        return self.__name

    @name.setter #meng-set value baru untuk name
    def name(self, val):
        print("anda mencoba mengubah name")
        # apabila val nya lebih dari 10 karakter maka raise exception
        if len(val) > 10:
            raise exception("name nya terlalu panjang")
        else:
         self.__name = val

    def calculate_total_price(self): #ini adalah method
        return self.__price*self.quantity #gak perlu parameters karena sudah tau

    def diskon(self):
        # self.price = self.price * Item.pembayaran (dikali denagn Item.pembayaran)
        self.__price = self.__price * self.pembayaran # (dikali denagn self.pembayaran)

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

    # @property (hanya bisa dibaca ktk dipanggil)
    # def readOnlyName(self):
    #     return "AAA"
        