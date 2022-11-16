# this is the shift number
number = 8
# this determines if the loop runs again
response = 1

while response == 1:
    message = input("Input Message You Would Like Encrypted: ")
    # this is for the new encrypted message
    encrypt = ''
    # this is for the new decrypted message
    decrypt = ''
    # we go character by character to encrypt
    for letter in message:
        # only performs on lowercase letters
        if letter.islower():
            # 97 is the unicode for lowercase letters
            # add number because we are encrypting the encryption
            # ord() converts the letters to unicode
            # chr() converts the shifter unicode back to letters
            encrypt += chr((ord(letter) - 97 + number) % 26 + 97)
        # only performs on uppercase letters
        elif letter.isupper():
            # 65 is the unicode for uppercase letters
            # add number because we are decrypting the encryption
            # ord() converts the letters to unicode
            # chr() converts the shifter unicode back to letters
            encrypt += chr((ord(letter) - 65 + number) % 26 + 65)
        # performs on anything other than a letter
        else:
            # you are adding the original character, not shifted
            encrypt += letter

    print("The user input a message", str(message) + ", by encrypting "
          "with shift cipher, the corresponding Encrypted message "
          "is,", encrypt)

    for letter in encrypt:
        # only performs on lowercase letters
        if letter.islower():
            # 97 is the unicode for lowercase letters
            # subtract number because we are decrypting the encryption
            # ord() converts the letters to unicode
            # chr() converts the shifter unicode back to letters
            decrypt += chr((ord(letter) - 97 - number) % 26 + 97)
        # only performs on uppercase letters
        elif letter.isupper():
            # 65 is the unicode for lowercase letters
            # subtract number because we are decrypting the encryption
            # ord() converts the letters to unicode
            # chr() converts the shifter unicode back to letters
            decrypt += chr((ord(letter) - 65 - number) % 26 + 65)
        # performs on anything other than a letter
        else:
            # you are adding the original character, not shifted
            decrypt += letter

    print("The encrypted message is", str(encrypt) + ", by decrypting "
          "with shift cipher, the corresponding Decrypted message "
          "is,", decrypt)

    # this is to reactivate the loop if the user chooses
    response = input("Would you like to encrypt/decrypt another message? "
                     "Type Y for yes or N for no: ")

    # converts the possible responses to numbers for the loop to process
    # Y or y continues the loop
    if response == "Y" or response == 'y':
        response = 1
    # N or n terminates the loop
    elif response == 'N' or response == 'n':
        response = 0
