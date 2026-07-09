numbers = []
palindrome = []

for i in range(20):
    numbers.append(int(input()))

for n in numbers:
    if str(n) == str(n)[::-1]:
        palindrome.append(n)

print("Palindrome Numbers:", palindrome)
print("Count:", len(palindrome))