# Koprekar's constant
def revert_number(n:int)->int:
    return int(str(n)[::-1])

def number_checkup(n:int)->bool:
    if len(n) != 4 or not n.isdigit():
        raise ValueError("input must be a string of 4 digits(including leading zeros)")
    
    unique_dgts = set(n)
    return len(unique_dgts)>=2

def calc_diff(n: int, rev: int)->int:
    return abs(n-rev)

def calculate_constant(n: int):
    pass