import tkinter

window = tkinter.Tk()  # Construct a top level Tk widget with Tcl interpreter. This is the window of the GUI.
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

FONT = ('Arial', 12, 'bold')
# Entry
entry = tkinter.Entry()
entry.config(width=15)
entry.grid(column=1, row=3)

# Entry
text = tkinter.Label()
text.config(text='Miles', font=FONT)
text.grid(column=3, row=3)

# Entry
text = tkinter.Label()
text.config(text='is equal to: ', font=FONT)
text.grid(column=0, row=5)

# Entry
result = tkinter.Label()
result.config(font=FONT)
result.grid(column=1, row=5)

# Entry
text = tkinter.Label()
text.config(text='Km', font=FONT)
text.grid(column=2, row=5)


def convert_miles_to_km():
    value = 1.609344 * float(entry.get())
    result.config(text=value)


# Entry
button = tkinter.Button(text='Calculate', command=convert_miles_to_km, font=('Arial', 9, 'bold'))
button.grid(column=1, row=6)

window.mainloop()
