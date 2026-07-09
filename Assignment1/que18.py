numbers = []
binary = []

for i in range(20):
    numbers.append(int(input()))

for n in numbers:
    temp = n

    if temp == 0:
        binary.append("0")
        continue

    b = ""

    while temp > 0:
        b = str(temp % 2) + b
        temp //= 2

    binary.append(b)

print(binary)