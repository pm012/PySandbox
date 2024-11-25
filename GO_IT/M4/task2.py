""""Remove extrime values from the list (min, max)"""

def prepare_data(data: list[int])->list: # O(nlog n) !!!
    data.remove(min(data))
    data.remove(max(data))

    return sorted(data)

#more eficient implementation:
def prepare_data_eficient(data: list[int]) -> list: # O( n log n), but no usless removes
    if not data or len(data) <= 2:
        return []

    # Find min and max
    min_val, max_val = min(data), max(data)

    # Remove min and max without sorting
    return [x for x in data if x != min_val and x != max_val]




def prepare_data1(data): # O(n log n + kn) where k is number of duplicates
    data.sort()
    
    while True:
        tmp = data[0]
        data.pop(0)        
        if tmp!=data[0]:
            break

    while True:
        tmp = data[len(data)-1]
        data.pop()        
        if tmp!=data[len(data)-1]:
            break
    return data


