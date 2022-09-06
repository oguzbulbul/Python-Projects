
import os 
import random
from ssl import ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION



art="""
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          
 """


def check_number(guess,number):
    if guess == number :
        return True
    elif guess > number :
        print("its too high !")
        return False
    elif guess < number :
        print("its too low :(")
        return False


def guess_the_number() :
    print(art)
    diff = input("which difficulty you want to play with 'easy' , 'medium' or 'hard' ?  ")
    print("easy : 1-100 between and 10 attempts\nmedium : 1-100 between and 7 attempts\nhard : 1-150 between and 6 attempts\n ")

    if diff == "easy" :
        attempts = 10
        number = random.randint(1,100)
        print(f"your attempts are : {attempts} and number is {number}")
    elif diff == "medium" :
        attempts = 7
        number = random.randint(1,100)
        print(f"your attempts are : {attempts} and number is {number}")
    elif diff == "hard" :
        attempts =6
        number = random.randint(1,150)
        print(f"your attempts are : {attempts} and number is {number}")
    
    guess=0
    while attempts !=0 and guess != number :
        guess = int(input("guess the numbeeerr "))
        if  not check_number(guess,number) :
            attempts -= 1
            print(f"you have {attempts} attenpts")
        elif check_number(guess,number) == True :
            print("you found it well done !")   
            break
    if attempts == 0 :
        print("you lost sorry")


keep_play = True
while keep_play == True :
    os.system('cls' if os.name == 'nt' else 'clear')
    guess_the_number()
    keep1_play = input("do you want to keep play 'y' or 'n' ")
    if keep1_play == 'y' :
        keep_play =True
    else :
        keep_play = False
