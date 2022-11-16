def count(s, ch):
    counts = 0
    # range of s
    for i in range(len(s)):
        # checks if a character occurs in s
        if s[i] == ch:
            counts += 1
    return counts


s = input("Enter a string: ")
ch = input("Enter a character: ")

appear = count(s, ch)

print(ch, "appears in", s, appear, "times")
