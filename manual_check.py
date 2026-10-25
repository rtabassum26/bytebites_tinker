
from models import Customer, FoodItem, Menu, Transaction

# 1. Create food items
burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
tea = FoodItem("Iced Tea", 3.25, "drinks", 4.0)
cake = FoodItem("Cheesecake", 5.99, "Desserts", 4.8)

# 2. Create and populate the menu
menu = Menu()

menu.add_item(burger)
menu.add_item(soda)
menu.add_item(tea)
menu.add_item(cake)

print("Full menu:", [item.name for item in menu.items])

# 3. Filter items by category
drinks = menu.filter_by_category("DRINKS")
print("Drinks:", [item.name for item in drinks])

desserts = menu.filter_by_category("Desserts")
print("Desserts:", [item.name for item in desserts])

missing = menu.filter_by_category("Breakfast")
print("Breakfast:", [item.name for item in missing])

# 4. Create a customer
customer = Customer("Alice")
print("Verified before purchase:", customer.is_verified_user())

# 5. Create a transaction
order = Transaction()
order.add_item(burger)
order.add_item(soda)
order.add_item(soda)

print("Ordered items:", [item.name for item in order.items])
print("Order total:", order.calculate_total())

# 6. Record the completed purchase
customer.add_purchase(order)

print("Verified after purchase:", customer.is_verified_user())
print("Purchase history count:", len(customer.purchase_history))

# Empty transaction
empty_order = Transaction()
print("Empty order total:", empty_order.calculate_total())

# Case-insensitive filtering
print(
    "Case-insensitive filtering:",
    menu.filter_by_category("drinks")
    == menu.filter_by_category("DRINKS")
)

# Independent customer histories
another_customer = Customer("Bob")
print("Bob verified:", another_customer.is_verified_user())