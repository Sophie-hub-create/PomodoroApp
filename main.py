
from tkinter import *
import tkinter.messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=0
cycles=0
checkmark=""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    global cycles
    global checkmark
    cycles =0
    checkmark=""
    window.after_cancel(timer)
    canvas.itemconfig(tomato_text, text="00:00")
    label_top.config(text="Timer", fg=GREEN)
    label_check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global cycles
    global checkmark
    cycles+=1
    label_check.config(text=f"{checkmark}")
    if cycles%8==0:
        label_top.config(text="Chill", fg=PINK)
        countdown(LONG_BREAK_MIN, 00)
    elif cycles%2==0:
        label_top.config(text="Break", fg=GREEN)
        countdown(SHORT_BREAK_MIN,00)
    else:
        label_top.config(text="Work", fg =RED)
        countdown(WORK_MIN, 00)
        checkmark+="✓"
        
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    
def countdown(minutes, seconds):
    global timer
    global checkmark
    if minutes >= 10:  
        if seconds >=10:
            canvas.itemconfig(tomato_text, text=f"{minutes}:{seconds}")
            timer = window.after(1000, countdown, minutes, seconds-1)
        elif seconds <10 and seconds>0:
            canvas.itemconfig(tomato_text, text=f"{minutes}:0{seconds}")
            timer = window.after(1000, countdown, minutes, seconds-1)
        elif seconds==0:
            canvas.itemconfig(tomato_text, text=f"{minutes}:0{seconds}")
            timer = window.after(1000, countdown, minutes-1, seconds+59)
    if minutes <10 and minutes >=0:
        if seconds >=10:
            canvas.itemconfig(tomato_text, text=f"0{minutes}:{seconds}")
            timer = window.after(1000, countdown, minutes, seconds-1)
        elif seconds <10 and seconds>0:
            canvas.itemconfig(tomato_text, text=f"0{minutes}:0{seconds}")
            timer = window.after(1000, countdown, minutes, seconds-1)
        elif seconds==0:
            canvas.itemconfig(tomato_text, text=f"0{minutes}:0{seconds}")
            timer = window.after(1000, countdown, minutes-1, seconds+59)
    if minutes==0 and seconds==0:
        
        start_timer()
        #tkinter.messagebox.showinfo("Timer Info",  "Your Timer is over")
        open_up()
    if cycles>8:
            reset()
           
           
# ---------------------------- POP-UP INFO ------------------------------- # 
def open_up():
    top=Toplevel(window)
    top.geometry('400x400')
    top.title("Timer Info")
    top.config(bg=YELLOW)
    Label(top, text="Keep on Focusing", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW).place(x=80,y=100)
    Button(top, text="Back to Timer", font=(FONT_NAME, 16, "bold"), fg=PINK, activeforeground=RED, background = YELLOW, activebackground=YELLOW, highlightthickness=2, command=top.destroy).place(x=100, y=200)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
tomato_text = canvas.create_text(110,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=2, column=2, ipady=25)

label_top = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
label_top.config(pady = 25)
label_top.grid(row=1, column=2)

button_left= Button(text="Start", font=(FONT_NAME, 18), fg=RED, background = YELLOW, activebackground=YELLOW, highlightthickness=2, activeforeground= GREEN,command=start_timer)
button_left.grid(row=3, column=1)

button_right= Button(text="Reset", font=(FONT_NAME, 18), fg=RED, background = YELLOW, activebackground=YELLOW, highlightthickness=2, activeforeground= GREEN,command=reset)
button_right.grid(row=3, column=3)

label_check= Label(font=( FONT_NAME, 35),fg=GREEN, bg=YELLOW)
label_check.config(pady=25)
label_check.grid(row= 4, column=2)

window.mainloop()