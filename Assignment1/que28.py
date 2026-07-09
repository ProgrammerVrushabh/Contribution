numbers = []

for i in range(15):
    numbers.append(int(input()))

# Mean
total = 0
for n in numbers:
    total += n

mean = total / 15

# Sort (Bubble Sort)
for i in range(15):
    for j in range(i + 1, 15):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

median = numbers[7]

# Mode
mode = numbers[0]
max_count = 0

for i in range(15):
    count = 0
    for j in range(15):
        if numbers[i] == numbers[j]:
            count += 1

    if count > max_count:
        max_count = count
        mode = numbers[i]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)