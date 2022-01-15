from Phone import Phone
from product import Product
# oop principles : encapsulation, abstraction, inherritance, polymorphism


# 3. polymorphism --> kemampuan untuk mengakses function dari class yang berbeda
phone1 = Product('Hanx980Pro', 100, 5)
phone1.pembayaran = 0.2
print(phone1.diskon()) #padahal tidak kita terapkan di phone.py ttp berjalan karena mewarisi sifat dari Class Item
       

