# Step 3
import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
hangmen = ['left leg', 'right leg', 'left arm', 'right arm', 'torso', 'head']

# Testing code
#print(f'Pssst, the solution is {chosen_word}.')
lives = len(hangmen) + 1  # Adding 1 here makes easier to display all stages.

# Create blanks
display = ['_'] * word_length
guesses = []

while '_' in display and lives > 0:
    # Check guessed letter
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f'You already guessed {guess}. Try again.')

    else:
        guesses.append(guess)

        # Reduce live if wrong guess
        if guess not in chosen_word:
            print('Your guess was wrong. Try again.')
            lives = lives - 1
            print(stages.pop(-1))

            if lives == 1:
                print('You only have one more chance!')

        # Check where guess is in chosen_word
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter  # Adds guess to display


        print(f"Chosen word: {' '.join(display)}")

# Print final message
if '_' not in display:
    print(f'The word was {chosen_word}')
    print('You won!')

if lives == 0:
    print('You lost!')


