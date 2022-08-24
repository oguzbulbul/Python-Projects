print("welcome to tip calculator !!")
bill=float(input("what was the total bill ? "))
people=int(input("how many people'll share the bill ? "))
tip=int(input("how much precentage would you like to give tip ? "))
bill=bill-(bill/100*tip)
eachone=bill/people
print(f"each people'll be pay {eachone}$ ")
