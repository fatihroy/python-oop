# create class
class Item:
    def calculate_total_price(self, a , b): #ini adalah method
        return a * b

item1 = Item()
item1.name = "book"
item1.price = 10
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))
      #self                          a            b

item2 = Item() 
item2.name = "pen"
item2.quantity = 3
item2.price = 100
print(item2.calculate_total_price(item2.price, item2.quantity))
