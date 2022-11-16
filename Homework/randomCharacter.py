import ASCIIcode

NUMBER_OF_CHARS = 175  # number of characters to generate
CHARS_PER_LINE = 25  # number of characters to display per line

for i in range(NUMBER_OF_CHARS):
    print(ASCIIcode.getRandomLowerCaseLetter(), end="")
    if (i + 1) % CHARS_PER_LINE == 0:
        print()

# coincides with ASCIIcode
