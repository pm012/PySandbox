def generator_numbers(string=""):
    is_curr_digit = False
    num = ""
    for ch in string:
        
        if ch.isdigit():
            is_curr_digit=True            
            num+=ch
        else:
            if is_curr_digit:
                is_curr_digit=False
                yield int(num)
                num = ""
    if is_curr_digit and num:
        yield int(num)
              


def sum_profit(string):
    sum = 0
    for num in generator_numbers(string):
        sum+=num
    return sum
        
    
    
        
if __name__ == "__main__":
    text = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
    print(sum_profit(text))