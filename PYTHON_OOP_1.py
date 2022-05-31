# OOP- OBJECTED ORIENTED PROGRAMMING
# CREATE A REUSABLE CODE
# DRY - DON'T REPEAY YOURSELF

class Item:
    def comp_total(self, x, y): # Method inside the class to receive the prince and qty.
        return x * y
        

item1 = Item()
item1.name = "Computer"
item1.price = 1000
item1.quantity = 5
print(item1.comp_total(item1.price, item1.quantity))

item2 = Item()
item2.name = "Keyboard"
item2.price = 200
item2.quantity = 3
print(item2.comp_total(item2.price, item2.quantity))

#print(type(item1)) # Class
#print(type(item1.name))
#print(type(item1.price))
#print(type(item1.quantity))