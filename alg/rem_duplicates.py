# Write a function to remove duplicates from a list without using set()

def remove_duplicates(my_list: list) -> list:
    res = []
    seen= {} # O(1) lookup complexity
    for item in my_list:
        #if item not in res: # O(N^2) complexity result without seen usage
        if item not in seen:
            res.append(item)
            seen[item]  = True # O(1)
            
    return res
    
    
    
if __name__ == "__main__":
    numbers = [1, 2, 8, 4, 8, 1, 10]
    words = ["apple", "banana", "orange", "apple", "cucumber"]
    
    print(remove_duplicates(numbers))
    print(remove_duplicates(words))