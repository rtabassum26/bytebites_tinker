from models import Customer, FoodItem, Menu, Transaction


def test_calculate_total_adds_item_prices():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
    transaction = Transaction()
    transaction.add_item(soda)
    transaction.add_item(burger)

    assert transaction.calculate_total() == 11.49


def test_empty_transaction_total_is_zero():
    transaction = Transaction()

    assert transaction.calculate_total() == 0.0


def test_filter_by_category_returns_only_matching_items():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
    tea = FoodItem("Iced Tea", 2.00, "Drinks", 3.9)
    menu = Menu()
    menu.add_item(soda)
    menu.add_item(burger)
    menu.add_item(tea)

    drinks = menu.filter_by_category("Drinks")

    assert [item.name for item in drinks] == ["Large Soda", "Iced Tea"]


def test_new_menu_has_no_items():
    menu = Menu()

    assert menu.items == []


def test_add_item_adds_food_item_to_menu():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    menu = Menu()

    menu.add_item(soda)

    assert [item.name for item in menu.items] == ["Large Soda"]


def test_add_item_keeps_items_in_order_added():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
    cake = FoodItem("Cheesecake", 4.75, "Desserts", 4.8)
    menu = Menu()

    menu.add_item(soda)
    menu.add_item(burger)
    menu.add_item(cake)

    assert [item.name for item in menu.items] == [
        "Large Soda",
        "Spicy Burger",
        "Cheesecake",
    ]


def test_filter_by_category_ignores_capitalization():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
    tea = FoodItem("Iced Tea", 2.00, "drinks", 3.9)
    menu = Menu()
    menu.add_item(soda)
    menu.add_item(burger)
    menu.add_item(tea)

    lowercase = menu.filter_by_category("drinks")
    capitalized = menu.filter_by_category("Drinks")
    uppercase = menu.filter_by_category("DRINKS")

    assert [item.name for item in lowercase] == ["Large Soda", "Iced Tea"]
    assert [item.name for item in capitalized] == ["Large Soda", "Iced Tea"]
    assert [item.name for item in uppercase] == ["Large Soda", "Iced Tea"]


def test_filter_by_category_returns_empty_list_when_no_match():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
    menu = Menu()
    menu.add_item(soda)
    menu.add_item(burger)

    desserts = menu.filter_by_category("Desserts")

    assert desserts == []


def test_filter_by_category_on_empty_menu_returns_empty_list():
    menu = Menu()

    drinks = menu.filter_by_category("Drinks")

    assert drinks == []


def test_filter_by_category_does_not_change_menu():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
    menu = Menu()
    menu.add_item(soda)
    menu.add_item(burger)

    menu.filter_by_category("Drinks")

    assert [item.name for item in menu.items] == ["Large Soda", "Spicy Burger"]


def test_food_item_stores_name_price_category_and_rating():
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)

    assert burger.name == "Spicy Burger"
    assert burger.price == 8.99
    assert burger.category == "Meals"
    assert burger.popularity_rating == 4.5


def test_add_item_adds_food_item_to_transaction():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    transaction = Transaction()

    transaction.add_item(soda)

    assert [item.name for item in transaction.items] == ["Large Soda"]


def test_calculate_total_counts_repeated_items():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    transaction = Transaction()
    transaction.add_item(soda)
    transaction.add_item(soda)

    assert transaction.calculate_total() == 5.00


def test_calculate_total_rounds_to_two_decimal_places():
    ketchup = FoodItem("Ketchup Packet", 0.10, "Condiments", 3.0)
    mustard = FoodItem("Mustard Packet", 0.20, "Condiments", 3.0)
    transaction = Transaction()
    transaction.add_item(ketchup)
    transaction.add_item(mustard)

    assert transaction.calculate_total() == 0.3


def test_calculate_total_updates_after_adding_item():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
    transaction = Transaction()
    transaction.add_item(soda)

    assert transaction.calculate_total() == 2.50

    transaction.add_item(burger)

    assert transaction.calculate_total() == 11.49


def test_new_customer_has_name_and_empty_purchase_history():
    customer = Customer("Alice")

    assert customer.name == "Alice"
    assert customer.purchase_history == []


def test_add_purchase_records_transaction_in_history():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    transaction = Transaction()
    transaction.add_item(soda)
    customer = Customer("Alice")

    customer.add_purchase(transaction)

    assert customer.purchase_history == [transaction]


def test_new_customer_is_not_verified():
    customer = Customer("Alice")

    assert customer.is_verified_user() is False


def test_customer_with_purchase_is_verified():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    transaction = Transaction()
    transaction.add_item(soda)
    customer = Customer("Alice")

    customer.add_purchase(transaction)

    assert customer.is_verified_user() is True


def test_customers_have_separate_purchase_histories():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    transaction = Transaction()
    transaction.add_item(soda)
    alice = Customer("Alice")
    bob = Customer("Bob")

    alice.add_purchase(transaction)

    assert alice.purchase_history == [transaction]
    assert bob.purchase_history == []


def test_customer_order_flow_from_menu_to_purchase():
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.99, "Meals", 4.5)
    tea = FoodItem("Iced Tea", 2.00, "Drinks", 3.9)
    menu = Menu()
    menu.add_item(soda)
    menu.add_item(burger)
    menu.add_item(tea)
    customer = Customer("Alice")

    drinks = menu.filter_by_category("Drinks")
    transaction = Transaction()
    for item in drinks:
        transaction.add_item(item)
    total = transaction.calculate_total()
    customer.add_purchase(transaction)

    assert [item.name for item in drinks] == ["Large Soda", "Iced Tea"]
    assert total == 4.50
    assert customer.purchase_history == [transaction]
    assert customer.is_verified_user() is True
