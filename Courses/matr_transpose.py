matrix_A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(*matrix_A) # unpacks matrix to 3 lists
#print(zip(*matrix_A)) usless

transpose = []
for rows in zip(*matrix_A): # get transposed row (regroup unpacked matrix lists)
    print(rows)
    transpose.append(list(rows)) # add rows to transposed matrix
print(transpose)