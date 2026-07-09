numbers = []
perfect_numbers = []

for i in range(15):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# perfect numbers
for num in numbers:
    if num > 1:
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i

        if sum == num:
            perfect_numbers.append(num)

print("\nPerfect Numbers:", perfect_numbers)
print("Total Perfect Numbers:", len(perfect_numbers))