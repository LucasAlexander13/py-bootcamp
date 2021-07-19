from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ordering = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

espresso = MenuItem('espresso', 50, 0, 18, 1.50)
latte = MenuItem('latte', 200, 150, 24, 2.50)
cappuccino = MenuItem('cappuccino', 250, 100, 24, 3.00)


while ordering:
    request = input(f'What would you like? ({menu.get_items()}): ')

    if request == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        if request == 'espresso':
            if coffee_maker.is_resource_sufficient(espresso):
                print('ahoy')
            else:
                print('nope')
        elif request == 'latte':
            if coffee_maker.is_resource_sufficient(latte):
                print('ahoy')
            else:
                print('nope')
        elif request == 'cappuccino':
            if coffee_maker.is_resource_sufficient(cappuccino):
                print('ahoy')
            else:
                print('nope')
