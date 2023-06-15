from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
machine = CoffeeMaker()
coin_machine = MoneyMachine()

def prepare_coffee(order_name: str, is_on: bool = True):
    order = menu.find_drink(order_name)

    payment = coin_machine.make_payment(order.cost)

    if payment < order.cost:
        print(f"Please add more coins to order a coffee.")
        return None
    if machine.is_resource_sufficient(order):
        coffee = machine.make_coffee(order)
        print(machine.report())
        return coffee

    else:
        return None

# user_input = str(input("What would you like? (espresso/latte/cappuccino): "))
# prepare_coffee(user_input)
