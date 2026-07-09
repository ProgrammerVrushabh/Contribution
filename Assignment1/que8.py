numbers = []

for i in range(25):
    numbers.append(int(input("Enter number: ")))

even_count = odd_count = 0
even_sum = odd_sum = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
        even_sum += n
    else:
        odd_count += 1
        odd_sum += n

print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)
print("Difference:", even_sum - odd_sum)