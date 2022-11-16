numberOfStudents = int(input("Enter the number of students: "))
lastScore = 0
highScore = 0
secondScore = 0
highName = "highName"
secondName = "secondName"

for i in range(numberOfStudents):
    name = input("Enter a student name: ")
    score = int(input("Enter a student score: "))
    if score > highScore and score > secondScore:
        highName = name
        highScore = score
    elif highScore >= score >= secondScore:
        secondName = name
        secondScore = score
    else:
        pass


print("Top two students:")
print(highName, "'s score is", highScore)
print(secondName, "'s score is", secondScore)
