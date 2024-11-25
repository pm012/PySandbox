"""Implement function loockup_key that will return all keys that will match parameter value"""

# task 5
def lookup_key(data: dict, value: str)->list:
    result = []
    for key, val in data:
        if val == value:
            result.append(key)
    return result

# task 6
"""There is a list of students with marks. You need to split the list into 2 parts. 
The first should contain students that contain <= of average and the second > average.
The function should return tuple of this 2 lists. Create split_list function that will take a list of integers founds average
and creates students that have <= of average and > average """

def split_list(grade: list)->tuple:
    less_avg, more_avg = [], []
    if len(grade) > 0: 
        avrage = sum(grade)/len(grade)                 
        for item in grade:
            if item <= avrage: 
                less_avg.append(item)
            else:
                more_avg.append(item)

    return (less_avg, more_avg) # O(n) complexity

# task 9
def is_valid_pin_codes(pin_codes):
    res = False
    if len(pin_codes)>0 and  len(pin_codes) == len(set(pin_codes)):
        for pin in pin_codes:
            if not isinstance(pin, str):
                return False
            elif len(pin) == 4 and pin.isdigit():
                res = True
            else:
                return False
               
    return res    
            
    

if __name__ == "__main__":
    print(split_list([1, 12, 3, 24, 5])) # -> ([1, 3, 5], [12, 24])









