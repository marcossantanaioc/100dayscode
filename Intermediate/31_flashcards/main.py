import tkinter
from tkinter import messagebox
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

canvas_width = 800
canvas_height = 526

data = pd.read_csv('data/french_words.csv').to_dict('records')


# Helper functions
def flip(word):
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(flash_label, text=word['English'], fill='white')


def read_flash_card():
    try:
        canvas.itemconfig(canvas_image, image=front_image)
        word = random.choice(data)
        canvas.itemconfig(flash_label, text=word['French'], fill='black')
        window.after(3000, flip, word)

        # Remove word if learned
        removed_item = data.remove(word)
        learned_data = pd.DataFrame(removed_item, index=[0])
        file_path = 'data/words_to_learn.csv'
        if os.path.exists(file_path):
            learned_data.to_csv(file_path, index=False, mode='a', header=None)
        else:
            learned_data.to_csv(file_path, index=False, mode='w')

    except IndexError:
        messagebox.askokcancel(title='Oops', message="You've learned all the words!")


def skip_flash_card():
    canvas.itemconfig(canvas_image, image=front_image)
    word_index = random.choice(range(len(data)))
    word = data[word_index]['French']
    canvas.itemconfig(flash_label, text=word, fill='black')


# Create window
window = tkinter.Tk()
window.config(width=1600, height=1200, bg=BACKGROUND_COLOR)
window.title('Flash Card App')

# Create canvas

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height, highlightthickness=2)
front_image = tkinter.PhotoImage(file='images/card_front.png')
back_image = tkinter.PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image((canvas_width + 2) / 2, (canvas_height + 2) / 2, image=front_image)
canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
canvas.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

# Buttons
right_image = tkinter.PhotoImage(file='images/right.png')
ok_button = tkinter.Button(image=right_image, command=read_flash_card, highlightthickness=0)
ok_button.grid(row=1, column=1)

# Buttons
wrong_image = tkinter.PhotoImage(file='images/wrong.png')
wrong_button = tkinter.Button(image=wrong_image, command=skip_flash_card, highlightthickness=0)
wrong_button.grid(row=1, column=0)

# Flash card Text
flash_label = canvas.create_text(400, 263, font=('Arial', 40, 'italic'))

window.mainloop()
