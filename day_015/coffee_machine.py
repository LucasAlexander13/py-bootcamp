from machine_resources import *
from os import system

def clear():
    return system('cls')

def request(order):
    clear()
    if order == 'report':
        report()
    elif order == 'refill':
        refill()
    elif order in MENU:
        if check(order):
            make(order, get_money())
        else:
            return print('No enough resources')
    else:
        print('Invalid input. Try again.')  

def check(coffee):
    for type in MENU[coffee]['ingredients']:
        if resources[type] < MENU[coffee]['ingredients'][type]:
            return False
    return True

def get_money():
    quarter = int(input('How many quarters?: ')) * 0.25
    dime = int(input('How many dimes?: ')) * 0.1
    nickel = int(input('How many nickels?: ')) * 0.05
    penny = int(input('How many pennies?: ')) * 0.01
    
    total_money = quarter + dime + nickel + penny
    return total_money

def change(coffee, money):
    money -= MENU[coffee]['cost']
    if money == 0:
        return print('You no have cash in change.')
    else:
        global machine_money 
        machine_money += MENU[coffee]['cost']
        return print(f'Here is ${money:.2f} in change.')

def make(coffee, money):
    if money < MENU[coffee]['cost']:
        return print('You are out of cash.')
    else:
        change(coffee, money)
    for type in MENU[coffee]['ingredients']:
        resources[type] -= MENU[coffee]['ingredients'][type]
    return print(f'Here is your {coffee}, enjoy!')

def report():
    for type in resources:
        if type == 'coffee':
            print(f'{type}: {resources[type]}g')
        else:
            print(f'{type}: {resources[type]}ml')
    print(f'Money: ${machine_money:.2f}')

def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    return print('Successfully stocked coffee machine.')

while True:
    order = input('What would you like? (espresso, latte, cappuccino): ')
    request(order.lower())
