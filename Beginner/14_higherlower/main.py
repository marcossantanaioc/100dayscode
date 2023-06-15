from game_data import data
import random
from art import logo, vs
from utils import clear

print(logo)

ANSWERS = {'A': 0, 'B': 1}


def format_data(data_dict: dict) -> str:
    """
    Returns a formated string for
    the information in `data_dict`
    Parameters
    ----------
    data_dict
        A dictionary with information about
        an entry in the game.

    Returns
    -------
        A formatted string.
    """
    article = 'a'
    name = data_dict['name']
    description = data_dict['description']
    if description[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        article = 'an'
    country = data_dict['country']

    formatted_info = f"{name}, {article} {description} from {country}"

    return formatted_info


def prepare_inputs(dataset: list) -> list:
    """
    Prepare input data for display.
    Parameters
    ----------
    dataset
        A list with information to be displayed.
    Returns
    -------
        A string representation for `data`
    """

    info_strs = []
    for info in dataset:
        info_strs.append(format_data(info))
    return info_strs


def compare(dataset: list, player_answer: str) -> int:
    """
    Checks the player's answer
    and computes the score.
    If the user gets the answer
    right, it will return either 0 or 1.
    Else, it will return -1.
    The numbers will be used by the game
    to decide which entry will be kept
    for the next round (index 0 or 1),
    or if the user lost the game (e.g. -1).

    Parameters
    ----------
    dataset
        A list with the current displayed data.
    player_answer
        The player's answer

    Returns
    -------
        The index of the correct answer (0 or 1)
        or -1 if the player guessed wrong.
    """

    answer = ANSWERS[player_answer]
    print(f"Player answer is {answer}")
    if (dataset[0]['follower_count'] > dataset[1]['follower_count']) and answer == 0:
        return 0
    elif (dataset[1]['follower_count'] > dataset[0]['follower_count']) and answer == 1:
        return 1
    else:
        return -1


def play():
    # Pick 2 random personalities for the game
    selected_data = random.sample(data, k=2)

    data.remove(selected_data[0])
    data.remove(selected_data[1])

    PLAY_GAME = True
    SCORE = 0
    while PLAY_GAME:

        selected_data_formated = prepare_inputs(selected_data)

        print(f"Compare A: {selected_data_formated[0]}")
        print(vs)
        print(f"Against B: {selected_data_formated[1]}")

        answer = str(input("Who has more followers? Type 'A' or 'B':"))
        result = compare(selected_data, answer)
        clear()

        if result >= 0:
            SCORE += 1
            print(f"You're right! Current score: {SCORE}")
            winner = selected_data.pop(ANSWERS[answer])
            if winner not in data:
                data.append(winner)

            new_competitor = random.choice(data)
            data.remove(new_competitor)
            selected_data.append(new_competitor)

        else:
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            PLAY_GAME = False
