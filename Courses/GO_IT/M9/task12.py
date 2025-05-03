'''payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
    
    rewrite the code above using reduce function'''
    
from functools import reduce
payment = [1, -3, 4]
def amount_payment1(payment):
    return reduce(lambda acc, value: acc + value if value > 0 else acc, payment, 0)

def amount_payment(payment): #better as filtering before reducing
    return reduce((lambda acc, value: acc + value), filter(lambda value: value > 0, payment))

def amount_payment2(payment): #more pythonic style
    # filter out negative values and sum the rest
    return sum(filter(lambda value: value > 0, payment))

if __name__ == "__main__":
    print(amount_payment(payment))
    print(amount_payment1(payment))

    
    
    