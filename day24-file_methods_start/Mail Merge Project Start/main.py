#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

#dosyadan davetl isimlerini çek
#çekilen isimleri uygun formatta yerleştir
#oluşan yazıyı yeni txt dosyası oluşturup oraya aktar


with open("/Users/Oğuz/Documents/vscode/project1/day24-file_methods_start/Mail Merge Project Start/Input/Names/invited_names.txt",mode="r") as names :
    name=names.read()
    namess=name.split("\n")
with open("/Users/Oğuz/Documents/vscode/project1/day24-file_methods_start/Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as template:
    letter=template.read()
    
print(namess)
# print(letter)
# x=letter.replace("[name],\n",name)
# print(x)
# letter_f.write(x)
for name in namess :
    textname="letter_for_"+name+".txt"
    print(textname)
    message=letter.replace("[name],\n",name)
    message=message.replace("Angela","Oguz :)")
    print(message)
    with open(f"/Users/Oğuz/Documents/vscode/project1/day24-file_methods_start/Mail Merge Project Start/Output/ReadyToSend/{textname}",mode="w") as letter_f:
        letter_f.write(message)


