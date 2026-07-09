numbers = []

for i in range(20):
    numbers.append(int(input("Enter number: ")))

visited = []

for n in numbers:
    if n not in visited:
        count = 0
        for x in numbers:
            if x == n:
                count += 1
        print(n, "=", count)
        visited.append(n)