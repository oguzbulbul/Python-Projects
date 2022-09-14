#coffee machine program

import os


logo = """
   _____       __  __            __  __            _     _            
  / ____|     / _|/ _|          |  \/  |          | |   (_)           
 | |     ___ | |_| |_ ___  ___  | \  / | __ _  ___| |__  _ _ __   ___ 
 | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
 | |___| (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
  \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                                      
                                                                      
"""
ingredients = {
"coffee" : 500,
"water" : 2000,
"milk" : 1000   
}


def take_order():
    order = input("what would u like to order sir espresso/latte/cappuccino/turkisch coffee ?  ").lower()
    return order



def report(ingredients) :
    
    coffee = ingredients["coffee"]
    water = ingredients["water"]
    milk = ingredients["milk"]
    print(f"coffee machine has {coffee}g coffee, {water}ml water and {milk}ml milk")


def check_resources(ingredients,ord_coff,ord_wat,ord_milk):
    
    mac_coffee = ingredients["coffee"]
    mac_water = ingredients["water"]
    mac_milk = ingredients["milk"]
    if mac_coffee >= ord_coff and mac_water >= ord_wat and mac_milk >= ord_milk :
        print("ingridients are valid sir !")
        return 0
    if mac_coffee < ord_coff :
        print("sorry coffee machine has not enough coffee :(")
    if mac_water < ord_wat :
        print("sorry coffee machine has not enough water :(")
    if mac_milk < ord_milk :
        print("sorry coffee machine has not enough milk :(")
           

def money_stuff(cost,insert):
    #valid insert
    if insert == cost :
        print("here's your coffee enjoy it :D")
        return 0
    elif insert > cost :
        changee = insert-cost
        print(f"here's your coffe and change {changee}$ :D ")
        return 0
    else :
        #invalid insert
        print("sorry its not enough :(")
        return 1



def coffee_machine():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print("welcome to coffee machine !!")
    keep_take=True
    casa=0
    while keep_take == True :
        order = take_order()
        if order == "off" :
            print("okey we're turning of it :(")
            return 0
        if order == "report" :
            report(ingredients)
            order = take_order()
        if order == "espresso" :
            #coffee=30, water=90, milk=0, cost=3$
            check=check_resources(ingredients,30,90,0)
            ingredients["coffee"] -= 30
            ingredients["water"] -= 90
            ingredients["milk"] -= 0
            if check == 0 :
                money1 = int(input("insert the money sir its 3$ "))
                a=money_stuff(3,money1)
                if a == 0 : 
                    casa += 3
        elif order == "latte" :
            #coffee=30, water=90, milk=220, cost=4$
            check=check_resources(ingredients,30,90,220)
            ingredients["coffee"] -= 30
            ingredients["water"] -= 90
            ingredients["milk"] -= 220
            if check == 0 :
                money2 = int(input("insert the money sir its 4$ "))
                a=money_stuff(4,money2)
                if a == 0 : 
                    casa += 4
        elif order == "cappuccino" :
            #coffee=30, water=90, milk=300, cost=5$
            check = check_resources(ingredients,30,90,300)
            ingredients["coffee"] -= 30
            ingredients["water"] -= 90
            ingredients["milk"] -= 300
            if check == 0 :
                money3 = int(input("insert the money sir its 3$ "))
                a=money_stuff(3,money3)
                if a == 0 : 
                    casa += 3
        elif order == "turkisch coffee" :
            #coffee=50, water=120, milk=0, cost=3,5$
            check = check_resources(ingredients,50,120,0)
            ingredients["coffee"] -= 50
            ingredients["water"] -= 120
            ingredients["milk"] -= 0
            if check == 0 :
                money4 = float(input("insert the money sir its 3.5$ "))
                a=money_stuff(3.5,money4)
                if a == 0 : 
                    casa +=  3.5
        print(f"cash box has {casa}$")
        keep_take=input("do you want to give an another order 'yes' or 'no' ?")
        if keep_take == "yes" :
            keep_take = True
        else :
            keep_take = False

coffee_machine()