__author__ = '13123035 - Jordan Harman'
# Import the 3 Ciphers used in the algorithm
import Caesar
import Rail_Fence
import Vigenere
# Import random to be used to generate the keys used in the caesar and rail key ciphers.
import random
# Import the hashlib module to use the sha256 algorithm to create the key used by the vigenere cipher.
import hashlib
# Import the base64 module which is used to turn the sha256 hash for the vigenere key into an ascii representation
import base64
# string letters is just an alphabet of characters a-z A-Z which is used to remove none alphabet characters from a key.
from string import letters
# import ceil which is used to determine how many blocks a message contains
from math import ceil


class Jordan_Harman_Algorithm_1:
    @staticmethod
    def get_caesar_key(key):
        random.seed(key)
        return random.randrange(1, 25)

    @staticmethod
    def get_rail_key(key):
        random.seed(key)
        return random.randrange(2, 16)

    @staticmethod
    def get_vigenere_key(key):
        text = base64.b64encode(hashlib.sha256(key).hexdigest())
        return ''.join([i for i in text if i in letters])

    @staticmethod
    def encrypt(message, key):
        message = Jordan_Harman_Algorithm_1.padding(message)
        if isinstance(message, list):
            results = list()
            for each_message in message:
                results.append(Jordan_Harman_Algorithm_1.__encrypt(each_message, key))
            return results

        elif isinstance(message, basestring):
            return Jordan_Harman_Algorithm_1.__encrypt(message, key)
        else:
            exit("Error encrypting data")

    @staticmethod
    def decrypt(message, key):
        message = Jordan_Harman_Algorithm_1.padding(message)
        if isinstance(message, list):
            results = list()
            for each_message in message:
                result = Jordan_Harman_Algorithm_1.decrypt(each_message, key)
                results.append(result)
            return results

        elif isinstance(message, basestring):
            results = "".join(Jordan_Harman_Algorithm_1.__decrypt(message, key))
            if chr(23) in results:
                result_index = results.index(chr(23))
                results = results[:result_index]
            return results

        else:
            exit("Error decrypting data")

    @staticmethod
    def __encrypt(message, key):
        # Split message in half
        Ln = message[:len(message) / 2]
        Rn = message[len(message) / 2:]

        # Get keys
        Rail_Fence_key = Jordan_Harman_Algorithm_1.get_rail_key(key)
        Caesar_key = Jordan_Harman_Algorithm_1.get_caesar_key(key)
        Vigenere_key = Jordan_Harman_Algorithm_1.get_vigenere_key(key)

        # Begin Rounds
        for x in range(0, 8):
            Rn = Vigenere.encrypt(Rn, Vigenere_key)
            Rn = Rail_Fence.encrypt(Rn, Rail_Fence_key)
            Rn = Caesar.encrypt(Rn, Caesar_key)
            Ln, Rn = Rn, Ln
        return Ln + Rn

    @staticmethod
    def __decrypt(message, key):
        # Split message in half
        B = message[:len(message) / 2]
        C = message[len(message) / 2:]

        Rail_Fence_key = Jordan_Harman_Algorithm_1.get_rail_key(key)
        Caesar_key = Jordan_Harman_Algorithm_1.get_caesar_key(key)
        Vigenere_key = Jordan_Harman_Algorithm_1.get_vigenere_key(key)

        # Begin Rounds
        for x in range(0, 8):
            C = Caesar.decrypt(C, Caesar_key)
            C = Rail_Fence.decrypt(C, Rail_Fence_key)
            C = Vigenere.decrypt(C, Vigenere_key)
            B, C = C, B
        return B + C

    @staticmethod
    def padding(plaintext):
        result = plaintext
        if isinstance(plaintext, basestring):
            # if the plaintext is 64
            if len(result) is 0:
                exit("Error: No message provided")
            elif len(result) is 64:
                return result
            # if the plaintext is less than 64
            elif len(result) < 64:
                # if result is 63 charactes long, just add the delimeter
                if len(result) == 63:
                    return result.join(chr(23))
                # if the plaintext is less than 63, add the delimeters and cycle through the plaintext adding it to the end
                elif len(result) < 63:
                    result += chr(23)
                    count = 0
                    while len(result) != 64:
                        result += (plaintext[count])
                        count += 1
                        if count > len(plaintext) - 1:
                            count = 0
                    return result
                else:
                    exit("Error")
            # if the plaintext is larger than 64 break it up into multiple blocks
            elif len(result) > 64:
                result_list = list()
                message_block_length = ceil((len(result) / 64.0))
                for each_block in range(0, int(message_block_length)):
                    temp = result[each_block * 64:each_block * 64 + 64]
                    result_list.append(Jordan_Harman_Algorithm_1.padding(temp))
                return result_list
            else:
                return False
        elif isinstance(plaintext, list):
            results = list()
            for each_block in result:
                results.append(Jordan_Harman_Algorithm_1.padding(each_block))
            return results

if __name__ == "__main__":
    Message = raw_input("Please enter the message to be encrypted: ")
    key = raw_input("Please enter the key: ")
    encrypted_message = Jordan_Harman_Algorithm_1.encrypt(Message, key)
    decrypted_message = Jordan_Harman_Algorithm_1.decrypt(encrypted_message, key)

    print "\nOriginal Message: \"{}\"" \
          "\nKey: \"{}\"" \
          "\n" \
          "\nEncrypted Text: {}\"" \
          "\nDecrypted Text: \"{}\"" \
          "".format(Message, key, encrypted_message, decrypted_message)
