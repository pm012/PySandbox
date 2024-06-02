matrix_A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(*matrix_A)
print(zip(matrix_A))

transpose = []
for rows in zip(*matrix_A):
    print(rows)
    transpose.append(list(rows))
print(transpose)