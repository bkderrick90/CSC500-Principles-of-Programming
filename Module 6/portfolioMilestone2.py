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


# Step 4: Build the ShoppingCart class with the following data attributes and related methods. Note: Some can
# be method stubs (empty methods) initially, to be completed in later steps
#
#     Parameterized constructor, which takes the customer name and date as parameters
#     Attributes
#     customer_name (string) - Initialized in default constructor to "none"
#     current_date (string) - Initialized in default constructor to "January 1, 2020"
#     cart_items (list)
#     Methods
#     add_item()
#         Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
#     remove_item()
#         Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
#         If item name cannot be found, output this message: Item not found in cart. Nothing removed.
#     modify_item()
#         Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
#         If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
#         If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
#     get_num_items_in_cart()
#         Returns quantity of all items in cart. Has no parameters.
#     get_cost_of_cart()
#         Determines and returns the total cost of items in cart. Has no parameters.
#     print_total()
#         Outputs total of objects in cart.
#         If cart is empty, output this message: SHOPPING CART IS EMPTY
#     print_descriptions()
#         Outputs each item's description.
#
# Example of print_total() output:
# John Doe's Shopping Cart - February 1, 2020
# Number of Items: 8
# Nike Romaleos 2 @ $189 = $378
# Chocolate Chips 5 @ $3 = $15
# Powerbeats 2 Headphones 1 @ $128 = $128
# Total: $521
#
# Example of print_descriptions() output:
# John Doe's Shopping Cart - February 1, 2020
# Item Descriptions
# Nike Romaleos: Volt color, Weightlifting shoes
# Chocolate Chips: Semi-sweet
# Powerbeats 2 Headphones: Bluetooth headphones

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


# Create items
item1 = ItemToPurchase("Nike Romaleos", "Volt color, Weightlifting shoes", 189, 2)
item2 = ItemToPurchase("Chocolate Chips", "Semi-sweet", 3, 5)
item3 = ItemToPurchase("Powerbeats 2 Headphones", "Bluetooth headphones", 128, 1)

# Create a shopping cart
cart = ShoppingCart("John Doe", "February 1, 2020")

# Add items to the cart
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

# Print total and descriptions
cart.print_total()
print()
cart.print_descriptions()

# Modify an item
item2_new = ItemToPurchase("Chocolate Chips", item_price=4, item_quantity=10)
cart.modify_item(item2_new)

# Remove an item
cart.remove_item("Nike Romaleos")

# Print updated total and descriptions
cart.print_total()
print()
cart.print_descriptions()

# Step 5: In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart
# parameter and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single
# character. Build and output the menu within the function.
# 
# If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement Quit before
# implementing other options. Call print_menu() in the main() function. Continue to execute the menu until the user
# enters q to Quit.
#
# Example:
# MENU
# a - Add item to cart
# r - Remove item from cart
# c - Change item quantity
# i - Output items' descriptions
# o - Output shopping cart
# q - Quit
# Choose an option:

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


def add_item_to_cart(cart):
    name = input("Enter the item name: ")
    description = input("Enter the item description: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item = ItemToPurchase(name, description, price, quantity)
    cart.add_item(item)


def remove_item_from_cart(cart):
    name = input("Enter the name of the item to remove: ")
    cart.remove_item(name)


def change_item_quantity(cart):
    name = input("Enter the name of the item to modify: ")
    quantity = int(input("Enter the new quantity: "))
    item = ItemToPurchase(item_name=name, item_quantity=quantity)
    cart.modify_item(item)


# Step 6: Implement Output shopping cart menu option. Implement Output item's description menu option.
#
# Example of shopping cart menu option:
# OUTPUT SHOPPING CART
# John Doe's Shopping Cart - February 1, 2020
# Number of Items: 8
# Nike Romaleos 2 @ $189 = $378
# Chocolate Chips 5 @ $3 = $15
# Powerbeats 2 Headphones 1 @ $128 = $128
# Total: $521
#
# Example of item description menu option.
# OUTPUT ITEMS' DESCRIPTIONS
# John Doe's Shopping Cart - February 1, 2020
# Item Descriptions
# Nike Romaleos: Volt color, Weightlifting shoes
# Chocolate Chips: Semi-sweet
# Powerbeats 2 Headphones: Bluetooth headphones

customer_name = input("Enter customer's name: ")
current_date = input("Enter today's date: ")

print(f"Customer name: {customer_name}")
print(f"Today's date: {current_date}")

cart = ShoppingCart(customer_name, current_date)
print_menu(cart)