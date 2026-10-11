#22 Add, transpose and multiply two matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
addition = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
transpose = [[A[j][i] for j in range(2)] for i in range(2)]
multiplication = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print("Addition:")
for row in addition:
    print(row)
print("Transpose:")
for row in transpose:
    print(row)
print("Multiplication:")
for row in multiplication:
    print(row)
