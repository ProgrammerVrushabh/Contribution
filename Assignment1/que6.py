numbers = []
armstrong = []

for i in range(20):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# for Armstrong numbers
for num in numbers:
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == num:
        armstrong.append(num)

# Display 
print("\nArmstrong Numbers:", armstrong)