
import random
import day7_art_wordlist

print(day7_art_wordlist.logo)
#comp choses a random word 
comp_word = random.choice(day7_art_wordlist.word_list)
#print(comp_word)
# and make that word covered !

covered_word=[]
for temp in range(0,len(comp_word)+1) :
    covered_word += "_"

for temp in range(0,len(comp_word)) :
    print(covered_word[temp] , end= " " )
print("\n")

# take a word guess from user and check it in the comp word
health=6
while health != 0 :
    #health=6
    print(day7_art_wordlist.stages[-health - 1])
    user_word=input("enter the word you guess : ").lower()

    counter=False
    for temp in range(0,len(comp_word)) :
        if user_word == comp_word[temp] :
            covered_word[temp]=user_word
            counter=True

    if counter == False :
        health-=1
    print(f"your health is {health}")

    for temp in range(0,len(comp_word)) :
        print(covered_word[temp] , end= " " )
    print("\n")