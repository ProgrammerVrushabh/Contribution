list1 = []
list2 = []

print("First Sorted List")
for i in range(10):
    list1.append(int(input()))

print("Second Sorted List")
for i in range(10):
    list2.append(int(input()))

merged = []
i = j = 0

while i < 10 and j < 10:
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < 10:
    merged.append(list1[i])
    i += 1

while j < 10:
    merged.append(list2[j])
    j += 1

print(merged)