import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

#cleaning terminal:
#os.system('cls' if os.name == 'nt' else 'clear')



def highest_dip(dippers_dic):
    highest_dip1=0
    for key in dippers_dic :
        for key1 in dippers_dic :
            if dippers_dic[key] > dippers_dic[key1] :
                highest_dip1=dippers_dic[key]
    #you found the highest dip now we're going to find dipper 
    #print(highest_dip1)

    for key2 in dippers_dic :
        if dippers_dic[key2] == highest_dip1 :
            return key2



keep_trade = True
dippers_dic={}

while keep_trade == True :
    print(logo) 
    print("Welcome to trade game !!\n")
    name=input("what is your name ? ").lower() #key
    dip=int(input("how much dip you want to do ? ")) #value
    
    ask = input("are there any other dippers ? type yes or no ").lower()
    if ask == "yes" :
        keep_trade=True
    elif ask == "no":
        keep_trade =False
    else :
        print("you should have type yes or no bitch")
        keep_trade=False

    dippers_dic[name]=dip
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")

print(dippers_dic)

print(f"Highest dip is {dippers_dic[highest_dip(dippers_dic)]}$ and dipper is {highest_dip(dippers_dic)} yeah you won !!")
