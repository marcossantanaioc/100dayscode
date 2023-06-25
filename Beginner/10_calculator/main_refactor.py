import tkinter


window = tkinter.Tk()
window.title('Calculator')
window.config(width=2000, height=2000)

# Result text
result_text = tkinter.Label(text='0', font=('Arial', 56, 'bold'))
result_text.grid(column=3, row=0, columnspan=2)

expression = ""

# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    result_text.config(text=expression)


# Create canvas
button1_image = tkinter.PhotoImage(file='images/1.png')
button1 = tkinter.Button(image=button1_image, text='1', highlightthickness=0, command=lambda : press(1))
button1.grid(row=0, column=0)

button2_image = tkinter.PhotoImage(file='images/2.png')
button2 = tkinter.Button(image=button2_image, highlightthickness=0, command=lambda x: press(2))
button2.grid(row=0, column=1)

button3_image = tkinter.PhotoImage(file='images/3.png')
button3 = tkinter.Button(image=button3_image, highlightthickness=0)
button3.grid(row=0, column=2)

button4_image = tkinter.PhotoImage(file='images/4.png')
button4 = tkinter.Button(image=button4_image, highlightthickness=0)
button4.grid(row=1, column=0)

button5_image = tkinter.PhotoImage(file='images/5.png')
button5 = tkinter.Button(image=button5_image, highlightthickness=0)
button5.grid(row=1, column=1)

button6_image = tkinter.PhotoImage(file='images/6.png')
button6 = tkinter.Button(image=button6_image, highlightthickness=0)
button6.grid(row=1, column=2)

button7_image = tkinter.PhotoImage(file='images/7.png')
button7 = tkinter.Button(image=button7_image, highlightthickness=0)
button7.grid(row=2, column=0)

button8_image = tkinter.PhotoImage(file='images/8.png')
button8 = tkinter.Button(image=button8_image, highlightthickness=0)
button8.grid(row=2, column=1)

button9_image = tkinter.PhotoImage(file='images/9.png')
button9 = tkinter.Button(image=button9_image, highlightthickness=0)
button9.grid(row=2, column=2)

add_image = tkinter.PhotoImage(file='images/add.png')
add_button = tkinter.Button(image=add_image, highlightthickness=0)
add_button.grid(row=2, column=3)

minus_image = tkinter.PhotoImage(file='images/minus.png')
minus_button = tkinter.Button(image=minus_image, highlightthickness=0)
minus_button.grid(row=2, column=4)

times_image = tkinter.PhotoImage(file='images/times.png')
times_button = tkinter.Button(image=times_image, highlightthickness=0)
times_button.grid(row=1, column=3)

division_image = tkinter.PhotoImage(file='images/division.png')
division_button = tkinter.Button(image=division_image, highlightthickness=0)
division_button.grid(row=1, column=4)


window.mainloop()
# def clear():
#     os.system('clear')
#
#

#
#
# def subtract(n1, n2):
#     """
#     Subtract `n1` from `n2`
#     Parameters
#     ----------
#     n1 : float or int
#       A float or int.
#     n2: float or int
#       Another float or int.
#     Returns
#     -------
#     result : float
#       `n1` - `n2`
#     """
#     res = n1 - n2
#     return res
#
#
# def multiply(n1, n2):
#     """
#     Multiply `n1` by `n2`
#     Parameters
#     ----------
#     n1 : float or int
#       A float or int.
#     n2: float or int
#       Another float or int.
#     Returns
#     -------
#     result : float
#       `n1` * `n2`
#     """
#     res = n1 * n2
#     return res
#
#
# def divide(n1, n2):
#     """
#     Divides `n1`by `n2`
#     Parameters
#     ----------
#     n1 : float or int
#       A float or int.
#     n2: float or int
#       Another float or int.
#     Returns
#     -------
#     result : float
#       `n1` / `n2`
#     """
#     res = n1 / n2
#     return res
#
#
# calculator = {'+': add,
#               '-': subtract,
#               '*': multiply,
#               '/': divide}
#
#
# def get_inputs():
#     num1 = float(input("What's the first number?: "))
#     num2 = float(input("What's the second number?: "))
#
#     for key in calculator:
#         print(key)
#     operation = str(input("Pick an operation from the line above?: "))
#
#     return num1, num2, operation
#
#
# def calculation(num1, num2, operation):
#     """
#     Run a given `operation`
#     on `num1` and `num2`
#     Parameters
#     ----------
#     num1 : float or int
#       A float or int.
#     num2: float or int
#       Another float or int.
#     operation : str
#         Mathematical operation run .
#     Returns
#     -------
#     result : float
#     """
#
#     do_calculation = True
#
#     while do_calculation:
#         func = calculator[operation]
#         result = func(num1, num2)
#         print(f"{num1} {operation} {num2} = {result}")
#
#         continue_calculation = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to exist.: "))
#
#         if continue_calculation == 'y':
#             clear()
#             num1 = result
#             num2 = float(input("What's the second number?: "))
#             operation = str(input("Pick an operation from the line above?: "))
#
#         else:
#             do_calculation = False
#             return result
