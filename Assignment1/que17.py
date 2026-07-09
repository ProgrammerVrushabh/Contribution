rows = 10

for i in range(rows):
    num = 1
    for j in range(rows - i):
        print(" ", end="")
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()