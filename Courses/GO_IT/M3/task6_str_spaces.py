"""

Create a format_string function to format the string. We pass the string string and length the length of the new string to the function. The function returns a new string according to the following algorithm:

    If the length of the original string is greater than or equal to the length, we return it in the same form;
    If it is less than length, we add spaces in front of the string in the amount (length - len(string)) // 2.

Tests for the correctness of the function are performed for the following sets of arguments:

    string='aaaaaaaaaaaaaaaaac', length=12
    length=15, string='abaa'

"""
def format_string(string, length):
    if len(string) >= length:
        return string
    else: 
        num = (length - len(string))//2
        print(num)
        space = ''
        for e in range(num):
            space +=' '
        return space+string
    
if __name__=="__main__":
    print(format_string("abaa", 15))
    print(format_string("aaaaaaaaaaaaaaaaac", 12))
    print(format_string("aaaaaaaaaaaaaaaaac", 3))