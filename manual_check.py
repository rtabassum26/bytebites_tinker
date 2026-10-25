
from models import FoodItem, Menu, Transaction, Customer

# Create sample food items
burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)

# Check FoodItem attributes
print("Food item:", burger.name)
print("Price:", burger.price)
print("Category:", burger.category)
print("Rating:", burger.popularity_rating)

# Create a menu
menu = Menu()
print("Menu items:", menu.items)

# Create a transaction
transaction = Transaction()
print("Transaction items:", transaction.items)

# Create a customer
customer = Customer("Alice")
print("Customer name:", customer.name)
print("Purchase history:", customer.purchase_history)

menu2 = Menu()
print("Independent menu lists:", menu.items is not menu2.items)

transaction2 = Transaction()
print("Independent transaction lists:", transaction.items is not transaction2.items)

customer2 = Customer("Bob")
print("Independent purchase histories:",
      customer.purchase_history is not customer2.purchase_history)