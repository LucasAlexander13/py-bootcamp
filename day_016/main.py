from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

def order(coffee):
    if coffee_maker.is_resource_sufficient(coffee):
        if money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)

while True:
    request = input(f'What would you like? ({menu.get_items()}): ')

    if request == 'report':
        coffee_maker.report()
        money_machine.report()

    elif request in ['latte', 'espresso', 'cappuccino']:
        order(menu.find_drink(request))
    
    elif request == 'refill':
        coffee_maker.resources = {'water': 300, 'milk': 200, 'coffee': 100}

    else:
        print('Invalid input.')
