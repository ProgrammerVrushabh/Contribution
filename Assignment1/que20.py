import math

numbers = []

for i in range(20):
    numbers.append(int(input()))

print("Number\tPrime\tEven/Odd\tSquare\tCube")

for n in numbers:

    if n > 1:
        prime = "Prime"
        for i in range(2, n):
            if n % i == 0:
                prime = "Composite"
                break
    else:
        prime = "Neither"

    even = "Even" if n % 2 == 0 else "Odd"

    square = "Yes" if int(math.sqrt(n)) ** 2 == n else "No"

    cube = "Yes" if round(n ** (1 / 3)) ** 3 == n else "No"

    print(n, "\t", prime, "\t", even, "\t", square, "\t", cube)