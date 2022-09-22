from lib2to3.pgen2 import driver
from optparse import Option
from secrets import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

keep_play=True
while keep_play :
    options=menu.get_items()
    choice=input(f"what would u like to order {options} ")
    if choice == "off" :
        keep_play = False
    elif choice ==  "report" :
        coffee_machine.report()
        money_machine.report()
    else :
        drink = menu.find_drink(choice)
        coffee_machine.is_resource_sufficient(drink)
