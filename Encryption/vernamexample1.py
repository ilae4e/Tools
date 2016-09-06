# Vernam cipher to encrypt and decrypt a sentence
import random
import string

def zeros(number):
    zstr = ""
    for i in range(number):
        zstr = zstr + "0"
    return zstr

sep = ""    	    	    	    	    	    	# separator between 8 bit blocks of the bit streams

random.seed(123456)  	    	    	    	    	# seed the randon number generator
sentence = raw_input('input a sentence to encrypt: ')

# Encryption
bitstream = []  	    	    	    	    	# list to hold bitstream to be encrypted
encrypted = []  	    	    	    	    	# list of encrypted bytes
enbitstream = []    	    	    	    	    	# list to hold encrypted bit stream
randbits = []   	    	    	    	    	# list to hold random bit stream
for i in range(len(sentence)):
    bits = 0
    for j in range(8):  	    	    	    	# generate 8 random bits to encrypt each letter
        bits += (random.randint(0,1))<<j
    letter = ord(sentence[i])
    encrypted.append(letter ^ bits) 	    	    	# encrypt the sentence 8 bits at a time

# Decryption
random.seed(123456) 	    	    	    	    	# reset to seed of the random number generator
decrypted = []  	    	    	    	    	# list to hold decrypted bytes
dbitstream = [] 	    	    	    	    	# list to hold decrypted bit stream
for i in range(len(encrypted)):
    bits = 0
    for j in range(8):
        bits += (random.randint(0,1))<<j
    decbits = encrypted[i] ^ bits   	    	    	# decrypt encrypted stream 8 bits at a time
    decrypted.append(chr(encrypted[i] ^ bits))
print string.join(decrypted,"")

