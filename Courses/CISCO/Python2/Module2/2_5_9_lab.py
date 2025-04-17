'''
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple – you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.
Test your code using the data we've provided.
19991229 => 6
20000101 => 4
'''

def calc_sum(str_nums: str)-> int:
    int_lst = [int(char) for char in str_nums]
    res = sum(int_lst)
    return res
    

def digit_of_life(b_date: str) -> int:
    """Calculate the digit of life (numerology) from an 8-digit birthdate string."""
    if len(b_date) != 8 or not b_date.isdigit():
        raise ValueError("Input must be an 8-digit string.")

    total = calc_sum(b_date)
    while total > 9:
        total = calc_sum(str(total))

    return total
        
        
if __name__ == "__main__":
    print(digit_of_life("23456789"))
    
    