List = []

# Accept 15 integers
for i in range(15):
    num = int(input("Enter an integer: "))
    List.append(num)


largest = List[0]
second_largest = List[0]
for num in List:
    if num > largest:
        largest = num
second_largest = None
for num in List:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num
print("\nList of Numbers:", List)
print("Largest Number:", largest)

if second_largest is not None:
    print("Second Largest Number:", second_largest)
else:
    print("Second Largest Number does not exist (all numbers are equal).")