alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift
#     if new_position > len(alphabet):
#       new_position -= len(alphabet)
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift
#     if new_position < 0:
#       new_position += len(alphabet)
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for char in start_text:
        if char not in alphabet:
            new_char = char
        else:
            position = alphabet.index(char)
            new_position = position + shift
            alphabet_size = len(alphabet) - 1
            if new_position > alphabet_size:
                new_position -= alphabet_size
            elif new_position < 0:
                new_position += alphabet_size
            # print(new_position)
            new_char = alphabet[new_position]

        end_text += new_char
    print(f"Here's the {direction}d result: {end_text}")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "yes":
        cipher_program()
    else:
        print("Goodbye")


def cipher_program():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # In case shift is greater than 26.
    shift = shift % len(alphabet)
    caesar(text, shift, direction)

import logo


print(logo.logo)
cipher_program()

# if direction == "e":
#   encrypt(text, shift)
# elif direction == "d":
#   decrypt(text, shift)
# else:
#   cipher_program()


##Dictionary
##Dictionary Comprehension?
##Slice
##Modulo revision


# #Shift alphabet
# shifted_alphabet = alphabet[shift:] + alphabet[:shift]
# cipher_dict = {{alphabet[i]}: {shifted_alphabet[i]} for i in range(len(alphabet)) }
#    for key in alphabet:
#     for value in shifted_alphabet:
#       cipher_dict[key] = value
# cipher_text = ""
# for char in text:
#     cipher_text += cipher_dict[char]
# print(cipher_text)