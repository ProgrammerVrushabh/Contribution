numbers = []

for i in range(20):
    numbers.append(int(input()))

for n in numbers:
    temp = abs(n)
    s = 0

    while temp > 0:
        s += temp % 10
        temp //= 10

    print(n, "=", s)