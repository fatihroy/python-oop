from Item import Item

item1 = Item('Item1', 313)
item1.name = 'item 244444ff' #bisa diubah karena ada setternya
# item1.name = 'item2' akan error
print(item1.name)
# item1.readOnlyName = "FFFF" akan error karena kita gak bisa set attribute dari readOnlyName

# akses Class Item
# Item.ambil_dariCSV()
# print(Item.product)


       

