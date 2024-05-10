def create_inventory():
  """Initializes an empty inventory dictionary."""
  return {}

def add_item(inventory, name, quantity):
  """Adds a new item or updates its quantity in the inventory."""
  inventory[name] = inventory.get(name, 0) + quantity

def remove_item(inventory, name, quantity):
  """Removes items from the inventory, reducing the quantity."""
  if name in inventory:
    inventory[name] -= quantity
    if inventory[name] <= 0:
      del inventory[name]

def get_quantity(inventory, name):
  """Returns the quantity of a specific item in the inventory."""
  return inventory.get(name, 0)

def generate_report(inventory, low_stock_threshold=5):
  """Generates a report on the inventory, including low stock alerts."""
  report = "Inventory Report:\n"
  for name, quantity in inventory.items():
    report += f"- {name}: {quantity}\n"
    if quantity <= low_stock_threshold:
      report += f"  **Low stock alert!**\n"
  return report

# Example usage
inventory = create_inventory()
add_item(inventory, "Apples", 10)
add_item(inventory, "Bananas", 15)
add_item(inventory, "Oranges", 5)
remove_item(inventory, "Bananas", 8)

print(generate_report(inventory))
