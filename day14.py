

import random
import os
from unicodedata import name
from day14data_art import data
from day14data_art import logo
from day14data_art import vs


def declare_option():
    """importing random option from data"""
    return random.choice(data)


def format(chosen_lib) :
    name = chosen_lib["name"]
    description = chosen_lib["description"]
    country = chosen_lib["country"]
    return f"{name} , a {description} from {country}"

def compare(guess,a_option,b_option):
    """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
    if a_option > b_option :
        return guess == "a"
    else :
        return guess == "b"






def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = declare_option()
  account_b = declare_option()

  while game_should_continue:
    account_a = account_b
    account_b = declare_option()

    while account_a == account_b:
      account_b = declare_option()

    print(f"Compare A: {format(account_a)}.")
    print(vs)
    print(f"Against B: {format(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = compare(guess, a_follower_count, b_follower_count)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()