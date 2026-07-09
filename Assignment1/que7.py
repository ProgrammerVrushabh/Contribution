fib = [0, 1]

while len(fib) < 30:
    fib.append(fib[-1] + fib[-2])

print("Fibonacci Numbers:", fib)

num = int(input("Enter number to search: "))

if num in fib:
    print("Found at position:", fib.index(num) + 1)
else:
    print("Not Found")