from tkinter import *
import math

GREY ="#A9A9A9"
YELLOW = "#f7f5dd"
GREEN = "#76EE00"
RED = "#e7305b"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
reset = None


# Timer reset
def reset_timer():
    window.after_cancel(reset)
    canvas.itemconfig(clock_text, text= "00:00")
    title_label.config(text="Timer")
    global reps
    reps = 0


# Timer mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="Break", fg=GREY)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

def count_down(timer):

    count_min = math.floor(timer / 60)
    count_sec = timer % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(clock_text, text=f"{count_min}:{count_sec}")
    if timer > 0:
        global reset
        reset = window.after(1000, count_down, timer - 1)
    else:
        start_timer()


# Creating the window

window = Tk()
window.title("Mr clock")
window.config(padx=50,pady=50, bg=YELLOW)
# Timer mechanism

# Creating Title

title_label =Label(text="Timer", fg=GREY, bg=YELLOW, font=(FONT_NAME, 50,"bold"))
title_label.grid(column=1, row=2)

# Importing the image

canvas = Canvas(width=500, height=500,bg=YELLOW, highlightthickness=0)
clock_img = PhotoImage(file="clock.png")
canvas.create_image(257, 257, image=clock_img)
clock_text = canvas.create_text(257,280, text="00:00", fill="white", font=(FONT_NAME, 60,"bold"))
canvas.grid(column=1, row=1)

# creating buttons
button_one = Button(text="Start", command=start_timer)
button_two = Button(text="Reset", command=reset_timer)
button_one.grid(column=1, row=3)
button_two.grid(column=1, row=4)








window.mainloop()






