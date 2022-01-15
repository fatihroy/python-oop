from Item import Item
# oop principles : encapsulation, abstraction, inherritance, polymorphism


# 1. encapsulation --> supaya tidak bisa akses langsung
item1 = Item('Item1', 313)
item1.__price = 5 #tidak bisa diset 

print(item1.price)



       

