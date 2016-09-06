__author__ = '13123035 - Jordan Harman'

import random
from string import letters

alphabet = letters[26:]


def encrypt(message, key):
    encrypted_message = ""
    for eachchar in message:
        num = alphabet.find(eachchar.upper())
        if num != -1:
            num += alphabet.find(alphabet[key])
            num %= len(alphabet)

            if eachchar.isupper():
                encrypted_message += alphabet[num]
            elif eachchar.islower():
                encrypted_message += alphabet[num].lower()
        else:
            encrypted_message += eachchar
    return encrypted_message


def decrypt(message, key):
    key = 26 - key
    return encrypt(message, key)
