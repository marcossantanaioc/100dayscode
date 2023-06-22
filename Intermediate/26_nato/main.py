import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key, value)


student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index, row)
    print(row.student, row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
phonetic_df = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {symbol.letter:symbol.code for _, symbol in phonetic_df.iterrows()}
print(phonetic_dict)
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_code_words = []

