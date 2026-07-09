numbers = []

for i in range(20):
    numbers.append(int(input()))

for i in range(20):
    for j in range(i + 1, 20):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Ascending:", numbers)

print("Descending:", numbers[::-1])