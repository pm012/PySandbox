# counting sort for decimals (complexity is the same as for bucket sort)

def counting_sort_decimals(numbers, precision=2):
    factor = 10 ** precision
    scaled_numbers = [int(num * factor) for num in numbers]
    
    max_val = max(scaled_numbers)
    count = [0] * (max_val + 1)
    
    for num in scaled_numbers:
        count[num] += 1
    
    sorted_numbers = []
    for i, freq in enumerate(count):
        sorted_numbers += [i] * freq
    
    sorted_numbers = [num / factor for num in sorted_numbers]
    return sorted_numbers

numbers = [4.25, 2.1, 2.0, 8.33, 3.5, 3.14, 1.0]
print("Unsorted array: ")
print(numbers)
sorted_numbers = counting_sort_decimals(numbers, precision=2)
print("Sorted by counting_sort for decimals, precision is 2")
print(sorted_numbers)
