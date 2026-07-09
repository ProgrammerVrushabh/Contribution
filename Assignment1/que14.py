numbers = []

for i in range(10):
    numbers.append(int(input()))

for n in numbers:
    print("\nTable of", n)
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)