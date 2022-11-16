score = input("Enter scores: ")

scores = score.split()

for i in range(0, len(scores)):
    scores[i] = int(scores[i])

max = max(scores)

array = range(len(scores))
y = 0
i = 0

for i in range(len(array)):
    if scores[i] >= (max - 10):
        print("Student", y, "score is", scores[i], "and grade is A")
        i += 1
        y += 1
    elif scores[i] >= (max - 20):
        print("Student", y, "score is", scores[i], "and grade is B")
        i += 1
        y += 1
    elif scores[i] >= (max - 30):
        print("Student", y, "score is", scores[i], "and grade is C")
        i += 1
        y += 1
    elif scores[i] >= (max - 40):
        print("Student", y, "score is", scores[i], "and grade is D")
        i += 1
        y += 1
    else:
        print("Student", y, "score is", scores[i], "and grade is F")
        i += 1
        y += 1
