# ByteBites Implementation Plan: Final (Task 2b)

All four classes will go in `models.py`. They match the class diagram in `bytebites_design.md`.

## 1. FoodItem

**Purpose:** Represents one item ByteBites sells, such as "Spicy Burger" or "Large Soda".

**Attributes:**

| Attribute | Type | Notes |
|---|---|---|
| `name` | `str` | e.g. `"Large Soda"` |
| `price` | `float` | Stored as a float (assumption A4) |
| `category` | `str` | A single category, e.g. `"Drinks"` |
| `popularity_rating` | `float` | Stored as a float (assumption A4) |

**Methods:** Only `__init__`. The diagram gives FoodItem no behavior, so it just holds data.

**Interactions:** FoodItem doesn't depend on any other class. Menu and Transaction both hold references to FoodItem objects, and the same object can be in the menu and in several transactions at once.

## 2. Menu

**Purpose:** The full list of items for sale, with filtering by category.

**Attributes:** `items: list[FoodItem]`, which starts as an empty list.

**Methods:**

- `add_item(item)` adds a FoodItem to `items` (assumption A3).
- `filter_by_category(category)` returns a **new list** of the items whose category matches, **ignoring capitalization**. For example, `"drinks"`, `"Drinks"` and `"DRINKS"` all return the same items. It leaves `items` unchanged and returns an empty list if nothing matches.

**Interactions:** Menu holds FoodItems but doesn't create or own them. It never refers to Customer or Transaction.

## 3. Transaction

**Purpose:** Groups the items a customer picked into one order and works out its total.

**Attributes:** `items: list[FoodItem]`, which starts as an empty list. Buying two of the same item means adding it twice.

**Methods:**

- `add_item(item)` adds a FoodItem to `items`.
- `calculate_total()` adds up `item.price` for every item and returns the sum **rounded to 2 decimal places**. The total is calculated fresh on every call and never stored (assumption A5). An empty transaction returns `0.0`.

**Interactions:** Transaction reads each FoodItem's `price`. It has no reference back to Customer.

## 4. Customer

**Purpose:** Stores a customer's name and past purchases, and reports whether they count as verified.

**Attributes:** `name: str`, `purchase_history: list[Transaction]`, which starts as an empty list.

**Methods:**

- `add_purchase(transaction)` adds a transaction to `purchase_history`. The calling code is responsible for passing only completed transactions (assumption A2), so this method does no checking.
- `is_verified_user()` returns `True` if `purchase_history` has at least one transaction, otherwise `False` (assumption A1). It isn't authentication and doesn't stop new customers from ordering.

**Interactions:** Customer holds Transactions through `purchase_history`. It never touches FoodItem or Menu directly.

## How the Pieces Fit Together

```
Menu ──holds──► FoodItem ◄──includes── Transaction ◄──purchase_history── Customer
```

1. Create FoodItems and add them to a Menu.
2. Browse the menu with `filter_by_category(...)`.
3. Create a Transaction and call `add_item(...)` for each item picked.
4. Call `calculate_total()`.
5. Call `customer.add_purchase(transaction)`. After this, `is_verified_user()` returns `True`.

## Build Order

1. FoodItem, since it has no dependencies.
2. Menu and Transaction, which depend only on FoodItem.
3. Customer, which depends on Transaction.

## Implementation Conventions

- **Public attributes** with no underscores and no getters or setters.
- Every list attribute starts as an empty list inside `__init__`, so each object gets its own list.
- Type hints and short docstrings, using only the standard library.
- No extra methods, input validation or classes beyond the diagram.

## Decisions Confirmed During Review

| # | Question | Decision |
|---|---|---|
| D1 | Private or public attributes? | Public attributes, to keep the implementation simple. |
| D2 | How should category filtering match? | Ignore capitalization, so variations in capitalization return the same results. |
| D3 | Should the total be rounded? | Round to 2 decimal places. |
| D4 | Should `add_purchase()` check that a transaction is completed? | No. The calling code passes only completed transactions (assumption A2). |
