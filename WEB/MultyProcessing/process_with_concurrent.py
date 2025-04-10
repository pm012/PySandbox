import concurrent.futures
import math
import os
import psutil

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
       
       sqrt_n = int(math.floor(math.sqrt(num)))
       for i in range(3, sqrt_n+1, 2):
           if num % i == 0:
               return False
       return True
    
if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(min(len(PRIMES), os.cpu_count())) as pex:
        for number, prime in zip(PRIMES, pex.map(is_prime, PRIMES)):
            print(f"{number} is  prime: {prime}")
    
    physical = psutil.cpu_count(logical=False)
    logical = psutil.cpu_count(logical=True)
    print(f"Physical cores: {physical}")
    print(f"Logical cores: {logical}")