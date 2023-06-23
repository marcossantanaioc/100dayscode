import random
import tkinter
from tkinter import messagebox
from tkinter.constants import END


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
class PasswordGenerator:
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def __init__(self, min_letters: int = 8,
                 max_letters: int = 10,
                 min_symbols: int = 2,
                 max_symbols: int = 4,
                 min_numbers: int = 2, max_numbers: int = 4):
        self.nr_letters = random.randint(min_letters, max_letters)
        self.nr_symbols = random.randint(min_symbols, max_symbols)
        self.nr_numbers = random.randint(min_numbers, max_numbers)

    def generate_password(self):
        char_list = [random.choice(self.LETTERS) for _ in range(self.nr_letters)]
        symbols_list = [random.choice(self.SYMBOLS) for _ in range(self.nr_symbols)]
        numbers_list = [random.choice(self.NUMBERS) for _ in range(self.nr_numbers)]

        password_list = char_list + symbols_list + numbers_list

        random.shuffle(password_list)

        new_password = ''.join(password_list)
        print(f"Your password is: {new_password}")
        password_name.insert(0, new_password)
        # pyperclip.copy(new_password)  Doesnt work on linux

        return new_password


passgenerator = PasswordGenerator()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file(info):
    with open('data.txt', 'a') as f:
        f.write(info + '\n')


def delete_entry():
    email_name.delete(0, END)
    password_name.delete(0, END)
    website_name.delete(0, END)


def add_new_entry():
    typed_email = email_name.get()
    typed_password = password_name.get()
    typed_website = website_name.get()

    if len(typed_password) == 0 or len(typed_website) == 0 or len(typed_email):
        messagebox.askokcancel(title='Oops', message="Please don't leave any fields empty.")
    else:
        info = f"{typed_website} | {typed_email} | {typed_password}"

        is_ok = messagebox.askokcancel(title='Title', message=f"Email :{typed_email}\n"
                                                              f"Password : {typed_password}\n"
                                                              f"Website : {typed_website}\n"
                                                              f"Is it ok?")
        if is_ok:
            save_file(info)
            delete_entry()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(width=600, height=600, bg='white', padx=50, pady=50)
window.title('Password Manager')

# Canvas
photo = tkinter.PhotoImage(file='logo.png')
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0, bg='white')
canvas.create_image(100, 100, image=photo, anchor='center')
canvas.grid(column=1, row=0)

# Labels
website = tkinter.Label(text="Website: ", bg='white')
website.grid(row=1, column=0)
email = tkinter.Label(text="Email/Username: ", bg='white')
email.grid(row=2, column=0)
password = tkinter.Label(text='Password: ', bg='white')
password.grid(row=3, column=0)

# Input boxes
website_name = tkinter.Entry(width=35)
website_name.grid(row=1, column=1, columnspan=2)
email_name = tkinter.Entry(width=35)
email_name.grid(row=2, column=1, columnspan=2)
email_name.insert(0, 'mvssantana@mail.com')
password_name = tkinter.Entry(width=35)
password_name.grid(row=3, column=1, columnspan=2)

# Buttons
gen_password = tkinter.Button(text="Generate password", bg='white', command=passgenerator.generate_password)
gen_password.grid(row=3, column=2)
add_password = tkinter.Radiobutton(text="Add", width=40, bg='white', command=add_new_entry)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
