from recipes import MENU
from configs import RESOURCES, UNITS
from utils import clear


def get_resource_report():
    """
    Returns a report on the coffee machine resources.
    Returns
    -------
        A string representation of the resources.
    """
    output = "CoffeeExpress Report:\n#####################\n"
    for key, item in RESOURCES.items():
        units = UNITS[key]
        if key != 'Money':
            item_units = f"{item}{units}"
        else:
            item_units = f"{units}{item}"

        output += f"{key.capitalize()}: {item_units}\n"
    return output


def check_resources(order: dict) -> int:
    """

    Parameters
    ----------
    order
        A coffee order in the format.
        {ORDER_NAME : {INGREDIENTS : {...}}}
    Returns
    -------
        If negative, it means a ingredient is missing
        from resources.
    """

    ingredients = order['ingredients']
    has_missing_ingredient = 0
    for key, item in ingredients.items():
        if item > RESOURCES[key]:
            has_missing_ingredient -= 1
            print(f"Sorry, not enough {key} to prepare your coffee.")

    return has_missing_ingredient


def input_order() -> tuple:
    """

    Returns
    -------
        Order name and cost.
        If any ingredient is missing,
        the order will be cast as False.
    """
    order_type = str(input("What would you like? (espresso/latte/cappuccino): "))
    order = MENU[order_type]
    cost = order['cost']
    total_amount = 0
    refund = 0

    if check_resources(order) >= 0:
        while total_amount < cost:
            money = float(input("Insert the money: "))
            total_amount += money

            if total_amount < cost:
                print(f"The price for {order_type} is {cost}\nSo far you've inserted {total_amount}")
            elif total_amount > cost:
                refund += (total_amount - cost)
                print(f"We will refund you ${refund}")

        clear()
        return order_type, cost
    else:
        clear()
        return False, cost


def make_coffee(ingredients: dict, cost: float) -> bool:
    """

    Parameters
    ----------
    ingredients
        Ingredients for the coffee.
        See the menu for an example.
    cost
        Cost of the coffee.
    Returns
    -------
        True if coffee was prepared.
        False if not.
    """
    has_ingredients = True

    # Reduce resources
    for key, item in ingredients.items():
        RESOURCES[key] -= item
        if RESOURCES[key] <= 0:
            RESOURCES[key] = 0
            has_ingredients = False
    RESOURCES['Money'] += cost

    if has_ingredients:
        return True
    else:
        return False


def get_refund(cost: float):
    """
    Subtract `cost` from RESOURCES.
    Parameters
    ----------
    cost
        Cost of the coffee.
    """

    RESOURCES['Money'] -= cost


def maintenance(turn_on: bool = True):
    if turn_on:
        return True
    else:
        print(f"Shutting down the coffee machine.")
        return False


def coffee_machine(turn_on: bool = True):
    """
    Coffee machine.
    This function creates a coffee machine
    and prepare a coffee for a user.
    Parameters
    ----------
    turn_on
        Whether to turn on or off the machine.

    """

    RUN = True
    if not turn_on:
        return maintenance(turn_on)

    while RUN:
        order_type, cost = input_order()
        if not order_type:
            RUN = False

        ingredients = MENU[order_type]['ingredients']
        has_coffee = make_coffee(ingredients, cost)

        if has_coffee:
            print(f"Here is your {order_type}. Enjoy!")
            another_order = str(input("Would you like to make another order? 'y' or 'n'"))
            clear()

            if another_order == 'n':
                RUN = False

        elif not has_coffee:
            print(f"We will refund you ${cost}")
            get_refund(cost)
            RUN = False


if __name__ == '__main__':
    turn_on = str(input("Turn on the coffee machine? 'on' or 'off'"))
    if turn_on == 'on':
        turn_on = True
    else:
        turn_on = False
    coffee_machine(turn_on=turn_on)
