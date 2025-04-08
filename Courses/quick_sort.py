# (n log n) Complexity
def quick_sort_in_place(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively apply quick_sort to the partitions
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    # Select the pivot element
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1



def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Select the pivot element
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively apply quick_sort to the partitions
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
print("unsorted array: ")
print(numbers)
sorted_numbers = quick_sort(numbers)
print("Sorted by simple quick sort: ")
print(sorted_numbers)
numbers = [38, 27, 43, 3, 9, 82, 10]
quick_sort_in_place(numbers, 0, len(numbers) - 1)
print("Sorted array by in place quick sort - space eficient: ")
print(numbers)
