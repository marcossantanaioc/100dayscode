# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def transform_word():
    run = True
    output_list = []
    while run:
        try:
            word = input("Enter a word: ").upper()
            output_list.extend([phonetic_dict[letter] for letter in word])
            print(','.join(output_list))
            break
        except KeyError:
            print(f"Sorry, only letters in the alphabet.")
    return output_list


# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nj = transform_word()
print(nj)
