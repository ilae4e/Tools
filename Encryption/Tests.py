__author__ = '13123035 - Jordan Harman'

from Encryption import Jordan_Harman_Algorithm_1

message_lists = ([
    list(["Jordan Harman", "Charles"]),
    list(["Jordan Charles Harman Studies Computer Forensics and Security at Manchester Metropolitan University in the city of Manchester, He is in his Third year of his studies and is doing his dissertation with Doctor Robert Hegarty", "Manchester Metropolitan University"]),
    list(["123456789", "Number Test"]),
])

for each_message in message_lists:
    Message = each_message[0]
    key = each_message[1]

    encrypted_message = Jordan_Harman_Algorithm_1.encrypt(Message, key)
    decrypted_message = Jordan_Harman_Algorithm_1.decrypt(encrypted_message, key)

    print "------------------------------------------------------------------------------------------" \
          "\nOriginal Message: \"{}\"" \
          "\nKey: \"{}\"" \
          "\n" \
          "\nEncrypted Text: {}\"" \
          "\nDecrypted Text: \"{}\"" \
          "\n------------------------------------------------------------------------------------------"\
        .format(Message, key, encrypted_message, decrypted_message)