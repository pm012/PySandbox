# O(n log n) complexity
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    left_index, right_index = 0, 0

    # Merge the two halves while maintaining order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    # If there are remaining elements in left or right, append them
    sorted_arr.extend(left[left_index:])
    sorted_arr.extend(right[right_index:])

    return sorted_arr

# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted array: ")
print(numbers)
sorted_numbers = merge_sort(numbers)
print("Sorted by merge sort: ")
print(sorted_numbers)
