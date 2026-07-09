numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

rotation = 3

numbers = numbers[-rotation:] + numbers[:-rotation]

print(numbers)