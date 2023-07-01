import random
# Palindromes are words that are the same when one
# read left-to-right and right-to-left
# ex. ovo

# To check a palindrome we can reverse a given piece of text
# and compare it to the text in the initial order
# if they are the same, we have a palindrome

with open('palindromes.txt') as f:
    palindrome_inputs = [x.strip() for x in f.readlines()]


def check_palindrome(text: str):
    """
    Checks if a piece of text is a palindrome
    Parameters
    ----------
    text
        Text to check

    """
    text = text.lower().replace(' ', '').replace(',', '').replace('.', '')
    print(text)
    reversed_text = text[::-1]
    print(reversed_text)
    if reversed_text == text:
        print(f"{text} is a palindrome.")
    else:
        print('Not a palindrome')


# word = 'Ah. Satan sees Natasha'
# check_palindrome(word)

# Fibonacci sequence is a sequence of numbers where
# the next number is the sum of the previous 2 numbers

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b


# Bubble sort algorithm
# The bubble sort algorithm sorts a list
# by checking if sequential pairs of elements
# and swaps them if necessary.
my_list_ordered = list(range(0, 101))
my_list = random.sample(my_list_ordered, k=50)

for iteration in range(len(my_list)):
    for index in range(len(my_list) - 1):
        elem1 = my_list[index]
        elem2 = my_list[index + 1]
        if elem2 > elem1:
            my_list[index] = elem2
            my_list[index + 1] = elem1
            print(f"Just swap {elem1} with {elem2}")

print(my_list)