from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

espresso = MenuItem('espresso', 50, 0, 18, 1.50)
latte = MenuItem('latte', 200, 150, 24, 2.50)
cappuccino = MenuItem('cappuccino', 250, 100, 24, 3.00)
menu = {'espresso': espresso, 'latte': latte, 'cappuccino': cappuccino}

def order(coffee):
    coffee = menu[coffee]
    if coffee_maker.is_resource_sufficient(coffee):
        if money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)

while True:
    request = input(f'What would you like? ({menu.get_items()}): ')

    if request == 'report':
        coffee_maker.report()
        money_machine.report()

    elif request in menu:
        order(request)

    else:
        print('Invalid input.')
