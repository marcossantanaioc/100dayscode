rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

choices = ['rock', 'paper', 'scissors']

player_choice = input('Your pick: rock, paper or scissors?')

player_choice_index = choices.index(player_choice)

computer_choice = random.choice(choices)
computer_choice_index = choices.index(computer_choice)

rock_wins = [-2, 2]
paper_wins = [-1, 1]
scissors_wins = [1, -1]

print(f'Player chose {player_choice}')
print(f'Computer chose {computer_choice}')

diff = player_choice_index - computer_choice_index

if diff == 0:
    print('Draw.')

elif diff == -2:  # Rock vs scissors
    print('Player won!')

elif diff == 2 and player_choice == 'scissors':  # Scissors vs rock
    print('Player lost!')

elif diff == -1 and player_choice != 'scissors':  # Paper vs scissors
    print('Player lost!')

elif diff == 1 and player_choice == 'scissors':  # Scissors vs paper
    print('Player won!')

elif diff == 1 and player_choice == 'paper':  # Rock vs paper
    print('Player won!')
