import tkinter
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFFAD7".lower()
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    no_time = format_time(0)
    canvas.itemconfig(my_time, text=no_time)
    timer_text.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Time for a Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Time for a Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_text.config(text="Working hard!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def format_time(time_val):
    return time.strftime('%M:%S', time.gmtime(time_val))


def count_down(count):
    global check_mark
    canvas.itemconfig(my_time, text=format_time(int(count)))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps > 0 and reps % 2 == 0:
            check_mark += "✔"
        check_label.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(width=500, height=500, padx=100, pady=100, bg=YELLOW)

photo = tkinter.PhotoImage(file='tomato.png')
canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(101, 112, image=photo)
my_time = canvas.create_text(103, 125, text="00:00", font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(column=1, row=1)

# Timer text
timer_text = tkinter.Label(text='TIMER', font=(FONT_NAME, 56, 'bold'), fg='lightgreen', bg=YELLOW)
timer_text.grid(column=1, row=0)

# Start button
start_button = tkinter.Button(text='Start', font=(FONT_NAME, 20, 'bold'), bg='white', highlightthickness=0,
                              command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = tkinter.Button(text='Reset', font=(FONT_NAME, 20, 'bold'), bg='white', highlightthickness=0,
                              command=reset_timer)
reset_button.grid(column=2, row=2)

# Check mark
check_label = tkinter.Label(text='', font=(FONT_NAME, 20, 'bold'), bg=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=3)

window.mainloop()
