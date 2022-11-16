sentence = input("Enter a string: ")

aCount = 0
eCount = 0
iCount = 0
oCount = 0
uCount = 0
vowelCount = 0
consonantCount = 0

newSentence = sentence.replace(" ", "")

for char in newSentence:
    if char in "aA":
        aCount += 1
    if char in "eE":
        eCount += 1
    if char in "iI":
        iCount += 1
    if char in "oO":
        oCount += 1
    if char in "uU":
        uCount += 1
        consonantCount += 1
    else:
        consonantCount += 1

vowelCount = aCount + eCount + iCount + oCount + uCount
consonantCount = consonantCount - vowelCount

print("The number of vowels is", vowelCount)
print("The number of consonants is", consonantCount)