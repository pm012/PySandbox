'''
Let's return to calculating the price with a discount and analyze the approach from the position of currying. Create a discount_price(discount) function to define and return a function for calculating the actual price with a discount.

Calling the discount_price(discount) function will return a function calculating the price of an item with a discount equal to discount.

For example:

cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))
Should output the following:

85.0
90.0
95.0
'''


def cost_15(price: float)->float:
    return discount_price(15)

def cost_10(price: float)->float:
    return discount_price(10)

def cost_05(price: float)->float:
    return discount_price(5)




def discount_price(discount):
    def calculate_discount(price):
        return price*(1-discount)
    return calculate_discount


if __name__ == "__main__":
    cost_05 = discount_price(0.05)
    cost_10 = discount_price(0.10)
    cost_15 = discount_price(0.15)
    
    price = 100    
    print(cost_15(price))
    print(cost_10(price))
    print(cost_05(price))
    



