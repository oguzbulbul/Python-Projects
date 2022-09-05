import os 
logo = """
 _____________________
|  _________________  |
| | ogi's calc   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(num1,num2) :
    return num1 + num2
def subtract(num1,num2) :
    return num1 - num2 
def multiply(num1,num2) :
    return num1*num2
def divide(num1,num2) :
    return num1/num2

operator_dic={
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

keep_calc=True
while keep_calc == True :
    num1=float(input("type the first number pls"))
    opr=input("enter the operator pls '+' , '-' , '*' , '/' ") 
    num2=float(input("end the second number pls"))

    calc_opr=operator_dic[opr]
    result=calc_opr(num1,num2)
    answer=input(f"result is {calc_opr(num1,num2)} do you want to keep doing stuff with result yes,no or quit  ? ")
    if answer == "no" :
        os.system('cls' if os.name == 'nt' else 'clear')
    elif answer == "quit" :
        keep_calc=False
    elif answer == "yes" :
        opr=input("enter the operator pls '+' , '-' , '*' , '/' ") 
        calc_opr=operator_dic[opr]
        num2=float(input("end the second number pls"))
        answer=input(f"result is {calc_opr(result,num2)} do you want to keep doing stuff with result yes,no or quit  ? ")
    else :
        print("inaccurate enter end of the calculation bye")
        keep_calc = False