# O(n) complexity

numbers = [4, 2, 2, 8, 0, 3, 3, 1, 0]

def counting_sort(numbers):   
    max_val = max(numbers)
    count = [0] * (max_val + 1)   
    for num in numbers:
        count[num] += 1
    sorted_numbers = []
    for i, freq in enumerate(count):
        sorted_numbers += [i] * freq
    return sorted_numbers

print(counting_sort(numbers))
