# Steps 1 - 3 from Portfolio Milestone 1

class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


# Steps 4 - 6 from Portfolio Milestone 2

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        item_found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_description != "none":
                    cart_item.description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: """

    option = ""
    while option != 'q':
        print(menu)
        option = input().strip()

        if option == 'a':
            add_item_to_cart(cart)
        elif option == 'r':
            remove_item_from_cart(cart)
        elif option == 'c':
            change_item_quantity(cart)
        elif option == 'i':
            cart.print_descriptions()
        elif option == 'o':
            cart.print_total()
        elif option == 'q':
            print("Exiting the menu.")
        else:
            print("Invalid option, please try again.")

######################################################################################
# Combine all previous milestone steps (1 - 6) with the following additional tasks.
#
# *** Step 7 is last as steps 8 - 10 are functions that need to be defined first ***
#
# Step 8: Implement Add item to cart menu option.
#
# Example:
# ADD ITEM TO CART
# Enter the item name:
# Nike Romaleos
# Enter the item description:
# Volt color, Weightlifting shoes
# Enter the item price:
# 189
# Enter the item quantity:
# 2
#
def add_item_to_cart(cart):
    name = input("Enter the item name: ")
    description = input("Enter the item description: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item = ItemToPurchase(name, description, price, quantity)
    cart.add_item(item)

# Step 9: Implement remove item menu option.
#
# Example:
# REMOVE ITEM FROM CART
# Enter name of item to remove:
# Chocolate Chips
#
def remove_item_from_cart(cart):
    name = input("Enter the name of the item to remove: ")
    cart.remove_item(name)

# Step 10: Implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem()
# method.
#
# Example:
# CHANGE ITEM QUANTITY
# Enter the item name:
# Nike Romaleos
# Enter the new quantity:
# 3
def change_item_quantity(cart):
    name = input("Enter the name of the item to modify: ")
    quantity = int(input("Enter the new quantity: "))
    item = ItemToPurchase(item_name=name, item_quantity=quantity)
    cart.modify_item(item)


# Step 7: In the main section of your code, prompt the user for a customer's name and today's date. Output the name
# and date. Create an object of type ShoppingCart.
#
# Example:
# Enter customer's name:
# John Doe
# Enter today's date:
# February 1, 2020
# Customer name: John Doe
# Today's date: February 1, 2020
#

customer_name = input("Enter customer's name: ")
current_date = input("Enter today's date: ")

print(f"Customer name: {customer_name}")
print(f"Today's date: {current_date}")

cart = ShoppingCart(customer_name, current_date)
print_menu(cart)
