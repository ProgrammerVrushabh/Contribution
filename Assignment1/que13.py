numbers = []

for i in range(30):
    numbers.append(int(input()))

positive = negative = zero = 0

for n in numbers:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

print("Positive %:", positive * 100 / 30)
print("Negative %:", negative * 100 / 30)
print("Zero %:", zero * 100 / 30)