def isAnagram(s1, s2):
    if sorted(s1) == sorted(s2):
        statement = "are"
    else:
        statement = "are not"
    return statement


s1 = input("Enter a string s1: ")
s2 = input("Enter a string s2: ")

state = isAnagram(s1, s2)

print(s1, "and", s2, state, "anagrams")