from Item import Item
# oop principles : encapsulation, abstraction, inherritance, polymorphism


# 2. abstraction --> menyembunyikan informasi yang gak perlu dan menampilkan informasi yang perlu
item1 = Item('Item1', 313)

item1.__connect() #gak bisa akses karena ini private method
item1.kirim_email()



       

