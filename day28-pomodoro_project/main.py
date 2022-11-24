
# ---------------------------- CONSTANTS ------------------------------- #

from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
timer= None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(timer)
    title.config(text="Timer",font=(FONT_NAME,50),fg=GREEN, bg=YELLOW, highlightthickness=0)
    tick_labs.config(text="")
    canvas.itemconfig(timer_text,text="00.00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    work25=WORK_MIN*60
    break5=SHORT_BREAK_MIN*60
    break20=LONG_BREAK_MIN*60
    global reps
    if reps%2==1:
        count_down(work25)
        title.config(text="Work !",font=(FONT_NAME,50),fg=GREEN, bg=YELLOW, highlightthickness=0)
        reps+=1
    elif reps%2==0 and reps!=8:
        count_down(break5)
        title.config(text="Break",font=(FONT_NAME,50),fg=PINK, bg=YELLOW, highlightthickness=0) 
        reps+=1
    elif reps == 8 :
        count_down(break20)
        title.config(text="Break",font=(FONT_NAME,50),fg=RED, bg=YELLOW, highlightthickness=0)
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):


    min=math.floor(count/60)
    if min < 10 :
        min = f"0{min}"
    sec=count%60
    if sec < 10 :
        sec=f"0{sec}"

    canvas.itemconfig(timer_text,text=f"{min}.{sec}")
    if count > 0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else :
        start_timer()
        marks=""
        work_ses = math.floor(reps/2)
        for _ in range(work_ses):
            marks+="✔" 
        tick_labs.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="project1/day28-pomodoro_project/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(110,135,text="00.00",fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(column=1,row=1)


#✔ 

title=Label(text="Timer",font=(FONT_NAME,50),fg=GREEN, bg=YELLOW, highlightthickness=0)
title.grid(column=1,row=0)

start_button=Button(text="Start",command=start_timer,highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=timer_reset)
reset_button.grid(column=2,row=2)

tick_labs=Label(text="",fg=GREEN,bg=YELLOW,font=(25),highlightthickness=0)
tick_labs.grid(column=1,row=3)


window.mainloop()
