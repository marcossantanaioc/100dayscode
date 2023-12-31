import tkinter

window = tkinter.Tk()
window.title('Calculator')
window.config(width=2000, height=2000)

# Result text
result_text = tkinter.Label(text='0', font=('Arial', 56, 'bold'))
result_text.grid(column=3, row=0, columnspan=2)

expression = ""
previous_result = ""
has_result = False


# Function to update expression
# in the text entry box

def decimals():
    # TODO Add support for decimal points
    pass
    # global expression, has_result
    # if has_result:
    #     result_text.config(text=expression)
    #     if "+" in expression or "-" in expression or "*" in expression or "/" in expression:
    #         expression = expression + str(num)
    #         result_text.config(text=expression)
    #
    # else:
    #     expression = expression + str(num)
    #     result_text.config(text=expression)


def press(num):
    global expression, has_result
    if has_result:
        result_text.config(text=expression)
        if "+" in expression or "-" in expression or "*" in expression or "/" in expression:
            expression = expression + str(num)
            result_text.config(text=expression)

    else:
        expression = expression + str(num)
        result_text.config(text=expression)


def add():
    global expression
    expression = expression + " + "
    result_text.config(text=expression)


def minus():
    global expression
    expression = expression + " - "
    result_text.config(text=expression)


def multiply():
    global expression
    expression = expression + " * "
    result_text.config(text=expression)


def division():
    global expression
    expression = expression + " / "
    result_text.config(text=expression)


def equals():
    global expression, has_result
    if "+" in expression or "-" in expression or "*" in expression or "/" in expression:
        math_expression = expression + " = "
        res = str(eval(expression))
        math_expression = math_expression + res
        result_text.config(text=math_expression)
        expression = res
        has_result = True


def clear():
    global has_result, expression
    expression = ""
    has_result = False
    result_text.config(text=expression)


# Create canvas
button1_image = tkinter.PhotoImage(file='images/1.png')
button1 = tkinter.Button(image=button1_image, text='1', highlightthickness=0, command=lambda: press(1))
button1.grid(row=0, column=0)

button2_image = tkinter.PhotoImage(file='images/2.png')
button2 = tkinter.Button(image=button2_image, highlightthickness=0, command=lambda: press(2))
button2.grid(row=0, column=1)

button3_image = tkinter.PhotoImage(file='images/3.png')
button3 = tkinter.Button(image=button3_image, highlightthickness=0, command=lambda: press(3))
button3.grid(row=0, column=2)

button4_image = tkinter.PhotoImage(file='images/4.png')
button4 = tkinter.Button(image=button4_image, highlightthickness=0, command=lambda: press(4))
button4.grid(row=1, column=0)

button5_image = tkinter.PhotoImage(file='images/5.png')
button5 = tkinter.Button(image=button5_image, highlightthickness=0, command=lambda: press(5))
button5.grid(row=1, column=1)

button6_image = tkinter.PhotoImage(file='images/6.png')
button6 = tkinter.Button(image=button6_image, highlightthickness=0, command=lambda: press(6))
button6.grid(row=1, column=2)

button7_image = tkinter.PhotoImage(file='images/7.png')
button7 = tkinter.Button(image=button7_image, highlightthickness=0, command=lambda: press(7))
button7.grid(row=2, column=0)

button8_image = tkinter.PhotoImage(file='images/8.png')
button8 = tkinter.Button(image=button8_image, highlightthickness=0, command=lambda: press(8))
button8.grid(row=2, column=1)

button9_image = tkinter.PhotoImage(file='images/9.png')
button9 = tkinter.Button(image=button9_image, highlightthickness=0, command=lambda: press(9))
button9.grid(row=2, column=2)

add_image = tkinter.PhotoImage(file='images/add.png')
add_button = tkinter.Button(image=add_image, highlightthickness=0, command=add)
add_button.grid(row=2, column=3)

minus_image = tkinter.PhotoImage(file='images/minus.png')
minus_button = tkinter.Button(image=minus_image, highlightthickness=0, command=minus)
minus_button.grid(row=2, column=4)

times_image = tkinter.PhotoImage(file='images/multiplication.png')
times_button = tkinter.Button(image=times_image, highlightthickness=0, command=multiply)
times_button.grid(row=1, column=3)

division_image = tkinter.PhotoImage(file='images/division.png')
division_button = tkinter.Button(image=division_image, highlightthickness=0, command=division)
division_button.grid(row=1, column=4)

equal_image = tkinter.PhotoImage(file='images/equals.png')
equal_button = tkinter.Button(image=equal_image, highlightthickness=0, command=equals)
equal_button.grid(row=1, column=5)

clear_image = tkinter.PhotoImage(file='images/clear.png')
clear_button = tkinter.Button(image=clear_image, highlightthickness=0, command=clear)
clear_button.grid(row=2, column=6)

dot_image = tkinter.PhotoImage(file='images/dot.png')
dot_button = tkinter.Button(image=dot_image, highlightthickness=0, command=decimals)
dot_button.grid(row=2, column=5)

window.mainloop()
