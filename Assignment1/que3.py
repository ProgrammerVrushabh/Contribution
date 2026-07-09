matrix1,matrix2=[],[]
for i in range(3):
    row=[]
    for j in range(3):
        element=int(input(f"Enter element for row {i+1}, column {j+1}: ")) #user input
        row.append(element)
    matrix1.append(row)
print("Matrix:/n",matrix1)
for i in range(3):
    row=[]
    for j in range(3):
        element=int(input(f"Enter element for row {i+1}, column {j+1}: ")) #user input
        row.append(element)
    matrix2.append(row)
print("Matrix:/n",matrix2)
print("Addition of matrices:")
result=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(matrix1[i][j]+matrix2[i][j])
    result.append(row)
print("Result:/n",result)