numbers = []

print("Enter 29 numbers from 1 to 30:")

for i in range(29):
    numbers.append(int(input()))

for i in range(1, 31):
    if i not in numbers:
        print("Missing Number:", i)
        break