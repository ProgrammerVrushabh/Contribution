numbers = []

for i in range(20):
    numbers.append(int(input()))

for n in numbers:
    print(n, ":", len(str(abs(n))), "digits")