from tkinter import *
import math

##constants
my_image = "myimage.png"
check_mark = ""
WORK_MIN = 2 # testing - you can change this to whatever you want
SHORT_BREAK_MIN = 1 # testing - you can change this to whatever you want
LONG_BREAK_MIN = 2 # testing - you can change this to whatever you want
REPS = 0
WORK_LIST = [1,3,5,7] #reps work list
BREAK_LIST = [2,4,6] #reps break list
timer = None
GREEN = "#9bdeac" #encycolorpedia.com
YELLOW = "#f7f5dd"

##resets the timer
def reset_timer():
    global REPS
    timer_label.config(text="Focus") #reset the timer main label
    check_mark_label.config(text="") #reset mark
    canvas.itemconfig(timer_text, text = f"00:00") #set the timer to 00:00
    REPS = 0 #reset reps
    window.after_cancel(timer) #stops the timer
##start button
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60 #converts min to seconds
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS in WORK_LIST:
        # print("work") testing
        timer_label.config(text="Work") #display Work in the title
        count_down(work_sec) #engaging coundown method
    elif REPS in BREAK_LIST:
        # print("sbreak") testing
        timer_label.config(text="Short Break")
        count_down(short_break)
    elif REPS == 8:
        timer_label.config(text="Break")
        count_down(long_break)

##countdown
def count_down(count): #timer countdown
    global check_mark
    count_min = math.floor(count / 60) #it gets rid of decimals - round to the largest whole number, if 4.8 then it give us 4,
    count_sec = count % 60 #calculates seconds
    if count_sec <= 9:
        count_sec = f"0{count_sec}" #dynamic typing
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0: #auto stops the timer (if the count is no 0 then count - 1)
       global timer
       timer = window.after(1000, count_down,count - 1) #this method (after) is used to refresh the screen
    else:
        start_timer()
        if REPS in range(2,9,2): #adds the checkmark every 2 reps - when you have completed a session (work+break)
            check_mark += "✔"
            check_mark_label.config(text=check_mark)





##UI
window = Tk()
window.title("Focus Timer")
window.config(padx=100, pady=50, bg=YELLOW)


##image
canvas = Canvas(width=205, height=224, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file=my_image) #change
canvas.create_image(103,112, image=tomato_img) #change
timer_text = canvas.create_text(103, 130, text="00:00", fill=GREEN, font=("Times new roman",35,"bold"))
canvas.grid(column=1, row=1)

##Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

##Timer label and Check mark
timer_label = Label(text="Focus", font=("Times new roman", 50, "italic"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1, row=0)
timer_label.config(padx=30, pady=30)

check_mark_label = Label(font=("Arial", 24, "bold"),fg=GREEN,bg=YELLOW)
check_mark_label.grid(column=1, row=4)
check_mark_label.config(padx=10, pady=10)



window.mainloop()