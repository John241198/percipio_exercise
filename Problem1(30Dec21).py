"""
Problem 1:

You are given a matrix.  Print the transpose of the matrix. The transpose of a matrix is obtained by changing rows to
columns and columns to rows. In other words, transpose of a matrix A[][] is obtained by changing A[i][j] to A[j][i].
For example:

Let matrix be :
1 2
3 4

Then transpose of the matrix will be:
1 3
2 4

(a) Input matrix is 3x4
(b) Input matrix is 5x4
"""
try:
    rows = int(input("Enter number of row's:"))
    column = int(input("Enter the numer of column's:"))
    print("Enter matrix elements:")

    matrix = []
    for i in range(rows):
        a = []
        for j in range(column):
            a.append(int(input()))
        matrix.append(a)

    Tran_matrix = [[0 for i in range(rows)] for j in range(column)]

    for i in range(rows):
        for j in range(column):
            Tran_matrix[j][i] = matrix[i][j]
    print("Matrix")
    for i in matrix:
        print(i)
    print("Transpose matrix")
    for i in Tran_matrix:
        print(i)

except ValueError:
    print("Enter integer only!...")

#also done by
"""
rows = int(input("Enter number of row's:"))
column = int(input("Enter the numer of column's:"))
print("Enter matrix elements:")

matrix = []
for i in range(rows):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)
result = map(list, zip(*matrix))

print("Matrix")
for i in matrix:
    print(i)

print("Transpose matrix")
for i in result:
    print(i)
"""