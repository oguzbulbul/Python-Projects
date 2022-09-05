import os
import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def score(deck) :
    if sum(deck) > 21 and 11 in deck :
        deck.append(1)
        deck.remove(11)
        return sum(deck)
    if sum(deck) == 21 and len(deck) == 2 :
        #it means blackjack
        return 0
    return sum(deck)
 

def compare(user_deck, comp_deck):
    userscore = score(user_deck)
    compscore = score(comp_deck)
    if userscore > 21 and compscore > 21 :
        print("you both went over but in some way you lost again..")
        return 1
    elif compscore == userscore :
        print("you guys are same draw again!!!")
        return 2
    elif compscore == 0 :
        print("dealer has blackjack you lost bro :( ")
        return 1
    elif userscore == 0 :
        print("omg you have blackjack you won !!")
        return 0
    elif userscore > 21 :
        print("you went over you lost :(")
        return 1
    elif compscore > 21 :
        print("you won, dealer went over")
        return 0
    elif userscore > compscore :
        print("you won!!")
        return 0 
    else :
        print("you lost bro :d ")
        return 1


keep_play = True
ply = input("do u want to ply blackjack ? 'y' or 'n'    ")
while keep_play == True :
    
    if ply == 'n' :
        keep_play = False
    elif ply  == 'y' :
        print(logo)

        user_deck = []
        comp_deck = []
        for t in range(2) :
            user_deck.append(random.choice(cards))
            comp_deck.append(random.choice(cards))

        print(f" your cards are {user_deck} and your score is {score(user_deck)} \ndealer's cards are [{comp_deck[0]}, _] ")

        if score(user_deck) == 0 :
            print("you won")
        elif score(comp_deck) == 0 :
            print("you lost")
        else :
            offer = 'y'
            while score(user_deck) < 21 and offer !='n':
                offer=input("do u want to draw a card ? 'y' or 'n' ")
                if offer == 'y':
                    user_deck.append(random.choice(cards))
                    print(f"your deck is {user_deck} and your score is {score(user_deck)}")
                    if score(user_deck) > 21 :
                        print(f"your score is {score(user_deck)}, you lost")
                
            while score(comp_deck)< 18 :
                comp_deck.append(random.choice(cards))
                if score(comp_deck)>21 :
                    print(f"yo won,comp deck is {comp_deck} and score is {score(comp_deck)}")
            
        game=compare(user_deck,comp_deck)    

    ply = input("do u want to ply blackjack ? 'y' or 'n'    ")
    os.system('cls' if os.name == 'nt' else 'clear')


