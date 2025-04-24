DEFAULT_DISCOUNT = 0.05

def get_discount_price_customer(price: float, customer: dict)-> float:
   
    if customer.get('discount') is not None:
        return price * (1 - customer.get('discount'))
    return price * (1 - DEFAULT_DISCOUNT)  # Apply default discount if no specific discount is set

if __name__ == "__main__":
    customer1 = {"name": "Dima"}
    customer2 = {"name": "Boris", "discount": 0.15}
    customer3 = {'name': 'Olga', 'discount': 0}
    print(get_discount_price_customer(100, customer1))
    print(get_discount_price_customer(100, customer2))
    print(get_discount_price_customer(100, customer3))
    
    