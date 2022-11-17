
# with open("/Users/Oğuz/Documents/vscode/project1/day25/weather_data.csv",mode="r") as file :
#     data=file.read()
#     list=data.split("\n")
# print(list)

# import csv

# with open("/Users/Oğuz/Documents/vscode/project1/day25/weather_data.csv",mode="r") as file :
#     data=csv.reader(file)
#     temperatures=[]
#     for row in data:
#         temp=row[1]
#         if temp.isnumeric():
#             temperatures.append(temp)
#     print(temperatures)


import pandas as pd 
# data = pd.read_csv("/Users/Oğuz/Documents/vscode/project1/day25/weather_data.csv")
# print(data)
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
#print(data["temp"].mean())
# print(data["temp"].max())
# max_temp=data["temp"].max()
# print(data[data.temp == max_temp])

# data_list = {
#     "students" : ["Akif","Sule","Oguz"],
#     "scores" : [10,90,80]
# }
# data = pd.DataFrame(data_list)
# data.to_csv("day25/new_data.csv")

sqruel_count = {
    "Fur Color" : [],
    "Count": []
}

data = pd.read_csv("/Users/oguzhan/Documents/vscode/project1/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data["Primary Fur Color"].to_list()
for color in fur_data:
    if color in sqruel_count["Fur Color"] :
        pass
    else:
        sqruel_count["Fur Color"].append(color)

for color in  sqruel_count["Fur Color"]:
    count=0
    for clr in fur_data:
        if color == clr :
            count +=1
    sqruel_count["Count"].append(count)

df=pd.DataFrame(sqruel_count)
df.to_csv("day25/squirrel_counts.csv")
print(sqruel_count)
