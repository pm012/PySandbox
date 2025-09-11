# Write a function to remove duplicates from a list(tuple or string) without using set()

def remove_duplicates(my_collection) -> list:
    res = []
    seen= {} # O(1) lookup complexity
    input_data = []
    if type(my_collection) == str:
        input_data = list(my_collection)
    else:
        input_data = my_collection
    

    for item in input_data:
        #if item not in res: # O(N^2) complexity result without seen usage
        if item not in seen:
            res.append(item)
            seen[item]  = True # O(1)
            
    return res

def unique_in_order(some_data):
    """Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any 
    elements with the same value next to each other and preserving the original order of elements."""
    res = []
    seen= {} # O(1) lookup complexity
    input_data = []
    if len(sequence) == 0:
        return res
    if type(sequence) == str:
        if len(sequence)>0:
            input_data = list(sequence)
        else:
            return []
    else:
        input_data = sequence

    tmp = input_data[0]    

    for item in input_data:
        #if item not in res: # O(N^2) complexity result without seen usage
        if item not in seen:
            res.append(item)
            tmp = item
    
    
    
if __name__ == "__main__":
    #numbers = [1, 2, 8, 4, 8, 1, 10]
    #numbers = ['A', 'B', 'C', 'D', 'A', 'B']
    numbers = "AAAABBBCCDAABBB"
    words = ["apple", "banana", "orange", "apple", "cucumber"]
    
    #print(remove_duplicates(numbers))
    print(unique_in_order(numbers))
    #print(remove_duplicates(words))
   