import numpy as np

matrix = []

print("Enter 3x3 Matrix")

for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

matrix = np.array(matrix)

print(np.linalg.inv(matrix))