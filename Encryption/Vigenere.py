__author__ = '13123035 - Jordan Harman'
from string import letters

alphabet = letters[26:]


def encrypt(message, key):
    keyindex = 0
    encrypted_message = ""
    key = key.upper()

    for character in message:
        num = alphabet.find(character.upper())
        if num != -1:
            num += alphabet.find(key[keyindex])

            num %= len(alphabet)

            if character.isupper():
                encrypted_message += alphabet[num]
            elif character.islower():
                encrypted_message += alphabet[num].lower()

            keyindex += 1
            if keyindex == len(key):
                keyindex = 0
        else:
            encrypted_message += character
    return encrypted_message


def decrypt(message, key):
    keyindex = 0
    encrypted_message = ""
    key = key.upper()

    for character in message:
        num = alphabet.find(character.upper())
        if num != -1:
            num -= alphabet.find(key[keyindex])
            num %= len(alphabet)

            if character.isupper():
                encrypted_message += alphabet[num]
            elif character.islower():
                encrypted_message += alphabet[num].lower()

            keyindex += 1
            if keyindex == len(key):
                keyindex = 0
        else:
            encrypted_message += character
    return encrypted_message
