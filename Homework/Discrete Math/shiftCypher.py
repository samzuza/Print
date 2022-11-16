alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = input("Input Message You Would Like Encrypted: ")
newMessage = ''
decryptMessage = ''
encrypt = 8

for letter in message:
    # for lowercase letters
    letter = letter.lower()

    # checks if message is all letters
    if letter.isalpha():
        # shifts the letter up by 8
        shifter = alphabet.index(letter) + encrypt
        # reassigns the array indexes
        new = alphabet[shifter - 1]
        # adds the new letter to the newMessage
        newMessage += new
    # won't shift the following
    elif ' ' or '/t' or '/n' in letter:
        newMessage += letter
    elif letter.isnumeric():
        newMessage += letter
    else:
        print("An error took place in recording the message. Check input.\n")

print("The user input a message", str(message) + ", by encrypting "
          "with shift cipher, the corresponding Encrypted message "
          "is,", newMessage)


for letter in newMessage:
    # for lowercase letters
    letter = letter.lower()

    # checks if message is all letters
    if letter.isalpha():
        shifter = alphabet.index(letter) - (encrypt - 1)
        newer = alphabet[shifter]
        decryptMessage += newer
    # won't shift the following
    elif ' ' or '/t' or '/n' in letter:
        decryptMessage += letter
    elif letter.isnumeric():
        decryptMessage += letter
    else:
        print("An error took place in recording the message. Check input.\n")

print("The encrypted message is", str(newMessage) + ", by decrypting "
          "with shift cipher, the corresponding Decrypted message "
          "is,", decryptMessage)

