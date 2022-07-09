import math
import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)  # this way we can stop the which we previously started
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")# here we ue temconfig because itis present in canvas
    #title_label "Timer"
    title_label.config(text="Timer")
    #Reset check_marks
    check_mark.config(text="")
    #Now without writing the below lines of code the timer jumps from work to break or viceversa
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If its the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        # title_label.config(text="Break", fg=RED)
        title_label.config(text="Break", fg=RED)

    # if its the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    # If its the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:  # Dynamic typing example
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,
                             count - 1)  # currently it is the local variable but to make it global we have to declared it global as timer = none:
    else:
        start_timer()  # This will helps you to reset the timer when it reaches to 00:00 start to 05:00 break
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=300) # you an either use this to fixed the size of output window
window.config(padx=100, pady=50, bg=YELLOW)  # it changes the bg color of image layout
# count_down(5)

title_label = tkinter.Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)  # 200, 224 are both are the pixel of tomato image.
# highlightthickness is used to remove the edges of that importing photo
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,
                    image=tomato_img)  # this are the basic requirement of canvas.create_image but if you put 100 as a value of x then it cut the image little bit so i changes it to 103
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35,
                                                                            "bold"))  # firstly it just simply a canvas.create_text but ot work in timer mechnism we further add timer_text
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="START", highlightthickness=0, command=start_timer).grid(column=0, row=2)
reset_button = tkinter.Button(text="RESET", highlightthickness=0, command=reset_timer).grid(column=2, row=2)

check_mark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_mark.grid(column=1, row=3)
window.mainloop()
