# 4.	Write a function that will generate a matrix whose elements are '*', change the elements of the diagonal of
# the matrix, '#' symbol.

matrix = []

rangeOF = int(input("Input range of Matrix: "))

for i in range(rangeOF):
    row = []
    for j in range(rangeOF):
        row.append("*")
    matrix.append(row)
    matrix[i][i] = "#"

print(matrix)
