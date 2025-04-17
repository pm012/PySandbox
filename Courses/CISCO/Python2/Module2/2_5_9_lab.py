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

def calc_sum(str_num: str)-> int:
    int_list = [int(i) for i in str_num.split()]
    res = sum(int_list)
    return res
    

def digit_of_life(b_date: str)-> int:
    if (len(b_date)!=8) or not b_date.isdigit():
        raise ValueError
       
    else:
        pass
        
        
if __name__ == "__main__":
    digit_of_life("234")
    
    