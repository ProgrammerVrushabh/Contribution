list1 = []
list2 = []

print("First List")
for i in range(15):
    list1.append(int(input()))

print("Second List")
for i in range(15):
    list2.append(int(input()))

common = []

for n in list1:
    if n in list2 and n not in common:
        common.append(n)

print("Common Elements:", common)
print("Total:", len(common))