# O(n^2) complexity
arr = [2, 8, 9, 10, 3, 6, 23, 11, 1]

lenth = len(arr)
for i in range(lenth):
    for j in range(0, lenth-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j + 1], arr[j]

print(arr)