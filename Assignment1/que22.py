numbers = []
reverse = []

for i in range(15):
    numbers.append(int(input()))

for n in numbers:
    temp = n
    rev = 0

    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    reverse.append(rev)

print("Original:", numbers)
print("Reversed:", reverse)