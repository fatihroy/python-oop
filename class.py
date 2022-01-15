from Phone import Phone
# oop principles : encapsulation, abstraction, inherritance, polymorphism


# 3. abstraction --> mengizinkan kita reuse code dari class
phone1 = Phone('Hanx980Pro', 313, 9)

#gak akan error karena Phone mewarisi Item
print(phone1.calculate_total_price())
phone1.kirim_email() 


       

