# 97
ch = 'a'
print(ord(ch))

# 'b'
print(chr(98))

# 65
print(ord('A'))

# 'A'
print(chr(ord('A')))

# 32
print(ord('a') - ord('A'))

# 32
print(ord('d') - ord('D'))

# 'H'
offset = ord('a') - ord('A')
lowercase = 'h'
uppercaseLetter = chr(ord(lowercase)) - offset
print(lowercase)