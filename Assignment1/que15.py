numbers = []

for i in range(15):
    numbers.append(int(input()))

print("Magic Numbers:")

for num in numbers:
    temp = num

    while temp > 9:
        s = 0
        while temp > 0:
            s += temp % 10
            temp //= 10
        temp = s

    if temp == 1:
        print(num)