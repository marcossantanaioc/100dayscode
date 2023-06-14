import random

print("Welcome to the Number Guessing Game!")
print(""" /$$   /$$                         /$$                                  /$$$$$$                                                            
| $$$ | $$                        | $$                                 /$$__  $$                                                           
| $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$       | $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$      | $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/ /$$__  $$ /$$__  $$
| $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/      | $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ | $$$$$$$$| $$  \__/
| $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$            | $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$| $$_____/| $$      
| $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$            |  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$$$| $$      
|__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/             \______/  \______/  \_______/|_______/|_______/  \_______/|__/      
                                                                                                                                           
                                                                                                                                        """)
DIFFICULTY = {'easy': 10, 'medium': 5, 'hard': 2}


def get_number(low: int = 1, high: int = 3) -> int:
    print("I'm thinking about a number between 1 and 100.")
    return random.randint(low, high)


def guess_number():
    guess = int(input('Make a guess: '))
    return guess


def play():
    CONTINUE = True
    level = str(input("Choose a dificulty. Type 'easy', 'medium' or 'hard': "))
    lives = DIFFICULTY[level]
    number = get_number()
    print(f"The number is {number}")

    while CONTINUE or lives > 0:
        player_guess = guess_number()

        if player_guess == number:
            print(f'On spot! The number was {number}')
            CONTINUE = False

        elif player_guess > number:
            print('Too high.\nGuess again.')
            lives -= 1
            print(f"You have {lives} attemps remaining to guess the number.")

        elif player_guess < number:
            print('Too low.\nGuess again.')
            lives -= 1
            print(f"You have {lives} attemps remaining to guess the number.")

        if lives == 0:
            CONTINUE = False


play()
