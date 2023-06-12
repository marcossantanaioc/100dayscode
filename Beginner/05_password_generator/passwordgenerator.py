#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_choices = random.choices(range(len(letters)), k=nr_letters)
number_choices = random.choices(range(len(numbers)), k=nr_numbers)
symbol_choices = random.choices(range(len(symbols)), k=nr_symbols)

easy_password = ''
for letter in letter_choices:
    easy_password += letters[letter]

for number in number_choices:
    easy_password += numbers[number]

for symbol in symbol_choices:
    easy_password += symbols[symbol]

print(f'Easy password: {easy_password}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = ''
combinations = []
for letter in letter_choices:
    combinations.append(letters[letter])

for number in number_choices:
    combinations.append(numbers[number])

for symbol in symbol_choices:
    combinations.append(symbols[symbol])

random.shuffle(combinations)  # Shuffle the list of characters

for character in combinations:  # Create the password
    hard_password += character
print(f'Hard password: {hard_password}')