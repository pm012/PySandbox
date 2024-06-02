# O (n) - best scenario
# O ((n/k)^2) for each bucket
# O (n Log n) worst cenario, when all elements fall in a single bucket

def bucket_sort(arr):
    # Determine the number of buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # Insert elements into the buckets
    for num in arr:
        index = int(num * bucket_count)
        buckets[index].append(num)
    
    # Sort each bucket and concatenate the results
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

numbers = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Original array: ")
print(numbers)
sorted_numbers = bucket_sort(numbers)
print("Sorted array: ")
print(sorted_numbers)
