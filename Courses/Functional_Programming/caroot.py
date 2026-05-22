# Caroting is a process of wrapping a function with another function, which can modify its behavior.
from typing import Callable

def discount(discount_persentage: float)-> Callable[[float], float]:
    def discount_calc(price: float)-> float:
        res = price *(1-discount_persentage/100)
        return res
    
    return discount_calc


ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

print(ten_percent_discount(500))

print(twenty_percent_discount(500))
