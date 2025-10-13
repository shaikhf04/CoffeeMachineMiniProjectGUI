from data.menu import *
from exception.stock_exception import OutOfStockError
from logger import logger

# A dictionary to map coffee names to their recipe
recipes = {
    "Black Coffee": blackCoffee,
    "Latte": latte,
    "Cappuccino": cappuccino
}

def check_stock_availability(coffee_name):
    """Checks if there are enough ingredients in stock to make a given coffee.

    This function iterates through the recipe for the specified coffee and
    compares the required quantity of each ingredient against the available
    stock.

    Args:
        coffee_name (str): The name of the coffee to check (e.g., "Latte").

    Returns:
        bool: True if all ingredients are available in sufficient quantities.

    Raises:
        OutOfStockError: If any ingredient is insufficient in stock.
        ValueError: If the recipe for the specified coffee_name is not found.
    """
    recipe = recipes.get(coffee_name)
    if not recipe:
        raise ValueError(f"Recipe for {coffee_name} not found.")

    for required_item, required_quantity in recipe.items():
        instock_quantity = instock.get(required_item, 0)
        logger(f"Checking stock for {required_item}: Required {required_quantity}, In Stock {instock_quantity}")
        if required_quantity > instock_quantity:
            log_msg = f"Not enough {required_item} in stock to make {coffee_name}. \nRequired: {required_quantity}, In Stock: {instock_quantity}"
            logger(log_msg,"STOCK_ERROR")
            raise OutOfStockError(log_msg)
    logger(f"Stock is sufficient for {coffee_name}.")
    return True


def make_coffee(coffee_name):
    """Makes a coffee by checking stock and deducting ingredients.

    This function first verifies if there are sufficient ingredients available to
    prepare the specified coffee. If the stock is adequate, it proceeds to
    deduct the required ingredients from the inventory.

    Args:
        coffee_name (str): The name of the coffee to be made (e.g., "Latte").

    Raises:
        OutOfStockError: If there are not enough ingredients in stock.
        ValueError: If the recipe for the specified coffee_name is not found.
    """
    logger(f"Attempting to make {coffee_name}")
    check_stock_availability(coffee_name)  # This will raise an exception if stock is insufficient

    recipe = recipes.get(coffee_name)
    for required_item, required_quantity in recipe.items():
        instock[required_item] -= required_quantity
    
    logger(f"Successfully made {coffee_name}. \nUpdated stock:")
    for item, quantity in instock.items():
        logger(f"{item}: {quantity}")
