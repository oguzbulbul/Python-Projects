from tkinter import *

window=Tk()
window.title("miles to kilometers !")
window.minsize(width=200,height=75)
window.config(padx=15,pady=15)

# 4 + 1 label, 1 button,1 entry
#grid label
grid_label=Label(text=" ")
grid_label.grid(column=0,row=0)

#entry
entry=Entry(width=20)
entry.insert(END,0)
entry.grid(column=1,row=0)
input_num=float(entry.get())

#labels:
lab1=Label(text="miles",font=("Arial",10))
lab1.grid(column=2,row=0)

lab2=Label(text="is equal to", font=("Arial",10))
lab2.grid(column=0,row=1)

lab3=Label(text=input_num,font=("Arial",10))
lab3.grid(column=1,row=1)

lab4=Label(text="Km",font=("Arial",10))
lab4.grid(column=2,row=1)

#button
def calc_and_change():
    km_vers=float(entry.get())*(1.61)
    print(km_vers)
    lab3.config(text=km_vers)
button=Button(text="Calculate",command=calc_and_change)
button.grid(column=1,row=2)

window.mainloop()