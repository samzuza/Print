s = "welcome to python"
#false
print(s.isalnum())
#true
print("Welcome".isalpha())
#true
print("2012".isdigit())
#false
print("first number".isidentifier())
#true
print(s.islower())
#false
print(s.isupper())
#false
print(s.isspace())
#true
print(s.endswith("thon"))
#false
print(s.startswith("good"))
#3 starts at index[3]
print(s.find("come"))
#-1 prints if not found in string
print(s.find("become"))
#15 counts from right to left
print(s.rfind("o"))
#3 3 o's
print(s.count("o"))
#Welcome to python
s1 = s.capitalize()
print(s1)
#Welcome To Python
s2 = s.title()
print(s2)
#new england
s = "New England"
s3 = s.lower()
print(s3)
#NEW ENGLAND
s4 = s.upper()
print(s4)
#nEW eNGLAND
s5 = s.swapcase()
print(s5)
#New Haven
s6 = s.replace("England", "Haven")
print(s6)
#New England
print(s)
#ETETAB
s = "ABABAB".replace("AB", "ET", 2)
print(s)
#Welcome to Python\t
s = "  Welcome to Python\t"
s1 = s.lstrip()
print(s1)
#  Welcome to Python
s2 = s.rstrip()
print(s2)
#Welcome to Python
s3 = s.strip()
print(s3)