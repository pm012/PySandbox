# combined recursion using 2 functions to define if  number odd or even
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1) #call is odd


def is_odd(x):
    return not is_even(x) #call is even


print(is_odd(17))
print(is_even(23))
print(is_even(22))
