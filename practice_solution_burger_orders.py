# Name: Jacob Steffen
# Description: Mimics a simplified ordering system at In N Out

# remember the requirements were very vague, so any solution will likely 
# differ widely from this.

import random # just used to generate an order number

class MenuItem:
    def __init__(self, description, price):
        self.description = description
        self.price = price

class Order: # makes an order. Doesn't have any parameters (besides self) the way I wrote it here.
    def __init__(self):
        # there could technically be overlap in the order numbers here
        # if that really bugs you, look up the uuid library, or you
        # could code a check where it first checks all existing order_numbers and if it happens
        # to generate an order number that already exists, it could try again.
        self.order_number = random.randint(1000, 9999) 
        self.menu_items_list = []

    def get_info(self):
        order_total = 0
        for menu_item in self.menu_items_list: # this calculates the total price of the order based on all the items in it.
            order_total += menu_item.price
        
        return f"Order {self.order_number}: {len(self.menu_items_list)} item(s) for a total of ${order_total:.2f} "

# I just wrote a method that would allow the user to choose a menu item from a list supplied to it.
def choose_menu_item(menu_items):
    while True:
        try:
            print("\nMenu Items:")
            for i, item in enumerate(menu_items, start=1):
                print(f"{i}. {item.description}: {item.price}")
            choice = int(input("Choose a menu item by number: "))
            return menu_items[choice - 1]
        except:
            print("That's not a valid menu item, try again.\n")

# just made some menu items. I only chose to make combo items just to simplify it.
menu_items = [MenuItem("Double-Double w/ French Fries and Medium Drink", 8.35),
              MenuItem("Cheeseburger w/ French Fries and Medium Drink", 7.00),
              MenuItem("Hamburger w/ French Fries and Medium Drink", 6.65)]

# I chose to keep track of my orders in a dictionary so I could look them up by order id as the key
orders = {}

while True: # this will keep running until the user enters the quit option

    # show the current orders each time an action is taken
    print(f"\nCurrently there are {len(orders)} active order(s):")
    for order in orders.values():
        print("\t" + order.get_info())

    # provide options
    action = input("\nYour options are:\n1: Add order to queue\n2: Remove order from queue\n3: Quit program\nPlease enter a number: ")
    
    if action == "3":
        print("\nExiting program.")
        break # exit the program

    elif action == "1":
        response = "y"
        order = Order() # make a new Order object

        while response == "y": # repeatedly ask for more menuitems to be added as long as the user wants.
            chosen_menu_item = choose_menu_item(menu_items) # choose a MenuItem
            order.menu_items_list.append(chosen_menu_item) # add that MenuItem to the Order
            response = input("Do you want to add another menu item to the order? Enter y or n: ").lower() # see if they want to add more to the order

        orders[order.order_number] = order # add the order to the Queue
        print(f"Added {order.get_info()}") 

    elif action == "2": # lets the user remove an order
        try:
            order_number = int(input("Enter the order number to remove: "))
            # since I'm using a dictionary, they need to provide a key to remove the Order from the queue            
            orders.pop(order_number)
            print(f"\nOrder #{order_number} has been removed.")
        except:
            print("\nOrder not found.")

    else:
        print("\nInvalid option, please try again.")


