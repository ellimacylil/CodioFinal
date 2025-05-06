import sys

def ceasar_cipher(text, shift):
    hidden = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            hidden += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            hidden+= char

    return hidden

shift = int(sys.argv[1]) 
message = input("Enter a message: ")
hidden_message = ceasar_cipher(message, shift)
print("Encrypted message:", hidden_message)

