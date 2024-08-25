class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"{quantity} {item_name}(s) added to inventory.")

    def remove_item(self, item_name, quantity):
        if item_name not in self.items:
            print(f"Item {item_name} not found in inventory.")
            return

        current_quantity = self.items[item_name]
        if current_quantity < quantity:
            print(f"Requested quantity exceeds available quantity for item {item_name}")
            return

        self.items[item_name] -= quantity
        print(f"{quantity} {item_name}(s) removed from inventory.")

    def display_inventory(self):
        print("Current Inventory Status:")
        for item_name, quantity in self.items.items():
            print(f"{item_name}: {quantity}")


# Example usage:
inventory = Inventory()

# Adding items to inventory
inventory.add_item("Apple", 10)
inventory.add_item("Banana", 5)
inventory.add_item("Orange", 8)

# Displaying current inventory status
inventory.display_inventory()

# Removing items from inventory
inventory.remove_item("Apple", 3)
inventory.remove_item("Banana", 7)  # This will exceed available quantity
inventory.remove_item("Grapes", 4)  # Item not found

# Displaying updated inventory status
inventory.display_inventory()
