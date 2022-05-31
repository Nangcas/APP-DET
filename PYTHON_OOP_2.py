class Item:
    def __init__(self, name, price, quantity): # Automatically call action, benefit from OOP
        self.name = name
        self.price = price
        self.quantity = quantity

    def comp_total(self):
        return self.price * self.quantity

item1 = Item("Computer", 1000, 5)
item2 = Item("Keyboard", 200, 3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

print(item1.comp_total())
print(item2.comp_total())
