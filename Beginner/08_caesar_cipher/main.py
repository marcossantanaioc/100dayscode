alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'decode':
        shift_amount = -1 * shift_amount

    shifted_text = ''
    for letter in start_text:
        if letter.isalnum() and letter in alphabet:
            alphabet_idx = alphabet.index(letter)
            transformed_idx = alphabet_idx + shift_amount
            # Wrap the alphabet to go back to the start of the alphabet.
            # When tranformed_idx >= len(alphabet), we will force it to wrap
            # by getting the remainder of the division by len(alphabet).
            if transformed_idx >= len(alphabet):
                transformed_idx = transformed_idx % len(alphabet)
            shifted_text += alphabet[transformed_idx]
        else:
            shifted_text += letter

    print(f"The {direction}d text is {shifted_text}")


# Check if user wants to redo
redo = True
redo = str(input("Type 'yes' if you want to go again. Otherwise type 'no'"))

if redo == 'yes':
    redo = True
else:
    redo = False

while redo:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)