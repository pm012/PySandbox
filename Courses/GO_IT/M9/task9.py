'''
At the beginning of the fourth module, we solved the problem of utility payments. 
They were a list of payment with positive and negative values. 
Now, you should create a positive_values function and use the filter function to 
filter the payment list by positive values and return it from the function.

payment = [100, -3, 400, 35, -100]
'''

def positive_values(list_payment):
    res = list()
    for i in filter(lambda x: x>0, list_payment):
        res.append(i)
    return res

if __name__ == "__main__":
    payment = [100, -3, 400, 35, -100]
    print(positive_values(payment))

    for i in filter(lambda x: x%2, range(1, 10+1)):
        print(i)


