# Step 1: Build the ItemToPurchase class with the following specifications:
#   Attributes:
#       item_name (string)
#       item_price (float)
#       item_quantity (int)
#   Default constructor:
#       Initializes item's name = "none", item's price = 0, item's quantity = 0
#   Method
#       print_item_cost()
#
# Example of print_item_cost() output:
#   Bottled Water 10 @ $1 = $10

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        cost = round(self.item_price * self.item_quantity, 2)
        print(f"The total for {self.item_quantity} {self.item_name} at ${self.item_price} per item is: ${cost}.")


eggs = ItemToPurchase(item_name="Dozen Eggs", item_price=3.50, item_quantity=7)

eggs.print_item_cost()

# Step 2: In the main section of your code, prompt the user for two items and create two objects of the
# ItemToPurchase class
#
# Example:
#   Item 1
#   Enter the item name: Chocolate Chips
#   Enter the item price: 3
#   Enter the item quantity: 1
#   Item 2
#   Enter the item name: Bottled Water
#   Enter the item price: 1
#   Enter the item quantity: 10

item1 = ItemToPurchase
item2 = ItemToPurchase

item1.item_name = input("Enter item name: ")
item1.item_price = float(input("Enter item price: "))
item1.item_quantity = int(input("Enter item quantity: "))

item2.item_name = input("Enter item name: ")
item2.item_price = float(input("Enter item price: "))
item2.item_quantity = int(input("Enter item quantity: "))

# Step 3: Add the costs of the two items together and output the total cost
#
# Example:
#   Chocolate Chips 1 @ $3 = $3
#   Bottled Water 10 @ $1 = $10
#   Total: $13

item1_cost = item1.item_price * item1.item_quantity
item2_cost = item2.item_price * item2.item_quantity
grand_total = item1_cost + item2_cost

print(f"{item1.item_quantity} {item1.item_name} at ${item1.item_price: .2f} per item is: ${item1_cost: .2f}.")
print(f"{item2.item_quantity} {item2.item_name} at ${item2.item_price: .2f} per item is: ${item2_cost: .2f}.")
print(f"The combined total of both items is: ${grand_total: .2f}.")
