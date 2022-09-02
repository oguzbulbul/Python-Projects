
def encrypt(message,shift) : 
    #find the word's index in alphabet than add as shift number and change with that chracter
    encrypted_mes=[]
    for temp in range(0,len(message) ) :
        for temp1 in range(0 , 26) :
            if message[temp] == alphabet[temp1] :
                encrypted_mes += alphabet[temp1 + shift] 
    return encrypted_mes



def decrypt(message,shift) :
    decrypted_mes=[]
    for temp in range(0,len(message) ) :
        for temp1 in range(26 , 52) :
            if message[temp] == alphabet[temp1] :
                decrypted_mes += alphabet[temp1 - shift] 
    return decrypted_mes



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

submission=input("what would you like to do 'encrypt' or 'decrypt' ? ")

message = input("what is your message ? type here : ")
shift = int(input("how much chracter you would like to pass ?"))

if submission == "encrypt" :
    encrypted_message=encrypt(message,shift)
    print(f"your encrypted message is {encrypted_message}")
elif submission == "decrypt" :
    decrypted_message = decrypt(message , shift)
    print(f"your decrypted message is {decrypted_message}")
else :
    print("wrong enter")




                 
 