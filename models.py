# ByteBites Backend Models
#
# Customer: Stores customer information and purchase history.
# FoodItem: Represents a food item with its name, price, category, and popularity rating.
# Menu: Manages the collection of food items and supports category-based filtering.
# Transaction: Stores selected food items and calculates the total cost.


class FoodItem:
    """A single item sold by ByteBites, 
    such as "Spicy Burger" or "Large Soda".
    """

    def __init__(self, name: str, price: float, category: str, popularity_rating: float) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """The full collection of food items, 
    with filtering by category.
    """

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        pass

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return a new list of items in the given 
        category, ignoring capitalization.
        """
        pass


class Transaction:
    """A group of selected food items that make up 
    one order.
    """

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a selected food item to the transaction. 
        Add the same item again to buy more than one.
        """
        pass

    def calculate_total(self) -> float:
        """Return the total price of all items, 
        rounded to 2 decimal places.
        """
        pass


class Customer:
    """A ByteBites customer with a name and 
    a history of completed purchases.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.purchase_history: list[Transaction] = []

    def add_purchase(self, transaction: Transaction) -> None:
        """Add a completed transaction 
        to the customer's purchase history.
        """
        pass

    def is_verified_user(self) -> bool:
        """Return True if the customer 
        has at least one completed purchase. 
        This is not identity authentication.
        """
        pass
