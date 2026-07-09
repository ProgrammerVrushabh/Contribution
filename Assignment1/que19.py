names = []
marks = []

for i in range(10):
    names.append(input("Name: "))
    marks.append(int(input("Marks: ")))

rank = list(range(1, 11))

for i in range(10):
    for j in range(i + 1, 10):
        if marks[i] < marks[j]:
            marks[i], marks[j] = marks[j], marks[i]
            names[i], names[j] = names[j], names[i]

print("Rank\tName\tMarks\tGrade")

for i in range(10):
    if marks[i] >= 90:
        grade = "A"
    elif marks[i] >= 75:
        grade = "B"
    elif marks[i] >= 60:
        grade = "C"
    elif marks[i] >= 40:
        grade = "D"
    else:
        grade = "F"

    print(i + 1, "\t", names[i], "\t", marks[i], "\t", grade)