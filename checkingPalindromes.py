s = input("Enter a string ")

low = 0
high = len(s) - 1

isPalindrome = True
while low < high:
    if s[low] != s[high]:
        isPalindrome = False
        break

    low += 1
    high -= 1

if isPalindrome:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
