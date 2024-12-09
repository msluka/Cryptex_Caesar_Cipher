# Cryptex - Encrypt and Decrypt your text using Caesar Cipher method

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def check_command():
    while True:

        command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

        if command == "encode":
            return "encode"
        elif command == "decode":
            return "decode"
        else:
            print("Invalid command. Please type 'encode' or 'decode'.")
            continue

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_position %= len(alphabet)
            cipher_text += alphabet[new_position]
    return cipher_text

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_position %= len(alphabet)
            cipher_text += alphabet[new_position]
    return cipher_text




