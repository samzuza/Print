alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def shift(encrypt):
    # user message input
    message = input("Input Message You Would Like Encrypted: ")
    newMessage = ''

    # while letter is in the range of message
    for letter in message:
        # converts message to lowercase letters for encryption
        letter = letter.lower()

        # checks if message is all letters
        if letter.isalpha():
            # shifter is used to encrypt the message
            shifter = alphabet.index(letter) + encrypt
            # if shift is greater than z, loop to a
            if shifter > 26:
                shifter = shifter % 26
            # - 1 because arrays work where the last index is one less
            new = alphabet[shifter - 1]
            newMessage += new
        # won't shift the following
        elif ' ' or '/t' or '/n' in letter:
            newMessage += letter
        # checks for numbers
        elif letter.isnumeric():
            newMessage += letter

    print("The user input a message", str(message) + ", by encrypting "
          "with shift cipher, the corresponding Encrypted message "
          "is,", newMessage)

    decryptMessage = ''
    for letter in newMessage:
        # checks if message is all letters
        if letter.isalpha():
            # shifts opposite to the encryption to decrypt
            shifter = alphabet.index(letter) - (encrypt - 1)
            new = alphabet[shifter]
            decryptMessage += new
        # won't shift the following
        elif ' ' or '/t' or '/n' in letter:
            decryptMessage += letter
        # checks for numbers in the encrypted message
        elif letter.isnumeric():
            decryptMessage += letter

    print("The encrypted message is", str(newMessage) + ", by decrypting "
          "with shift cipher, the corresponding Decrypted message "
          "is,", decryptMessage)


# assigned the shift for encryption and decryption as 8
shift(8)