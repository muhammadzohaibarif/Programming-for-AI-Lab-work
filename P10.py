#an inventory class is made
class inventory:


#a dictionary is defined
    def __init__(self):
       self.items= {}

#add item function is defined

    def add_item(self,name,qty,price):
       self.items[name]= (qty,price)


#remove item function is defined
    def remove_item(self,name):
       if name not in self.items:
        raise KeyError(f"No item named {name}")
       del self.items[name]

#this fucntion performs two things, one it counts the items and other is it gives total value
    def print_items(self):
        print("Item count:", len(self.items))
        total_value = sum(qty * price for qty, price in self.items.values())
        print("Total value:", total_value)

        #object of the class
inventory = inventory()


#to open or read a file with open() is used 
with open("stock.txt", "r") as file:
    for line in file:
        try:
            name, quantity, price = line.strip().split(",")
            inventory.add_item(name, int(quantity), float(price))
        except ValueError:
            print(f"Skipping bad line: {line.strip()}")

#object is made here
inventory.print_items()
inventory.remove_item("pen")
inventory.print_items()

try:
    inventory.remove_item("laptop")
except KeyError as e:
    print("Error:", e)
    




   
      




