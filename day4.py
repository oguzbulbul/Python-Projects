import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_chosen=input("what is your choice rock, paper or scissors ?").lower()
if user_chosen == "rock" :
    user_chosen=rock
elif user_chosen == "paper" :
    user_chosen=paper
elif user_chosen == "scissors" :
    user_chosen = scissors

gametools=[rock,paper,scissors]
comp_chosen=gametools[random.randint(0,2)]
print(f"your choice is {user_chosen}")
print(f"computer's choice is {comp_chosen}")

print("LETS MAKE THEM COMPARE !!!\n")

if user_chosen==comp_chosen :
    print("rematch!")
elif user_chosen == rock:
    if comp_chosen == paper :
        print("You lost, computer wins!")
    elif comp_chosen == scissors :
        print("You win !!")
elif user_chosen == paper :
    if comp_chosen == rock :
        print("You win !!")
    elif comp_chosen == scissors:
        print("You lost, computer wins!")
elif user_chosen == scissors :
    if comp_chosen == rock :
        print("You lost, computer wins !")
    elif comp_chosen == paper :
        print("You win")