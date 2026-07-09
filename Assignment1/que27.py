numbers = []
unique = []

for i in range(25):
    numbers.append(int(input()))

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)