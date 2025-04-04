import math
def dictionary_sample():
    dictionary = {}
    my_list = ['a', 'b', 'c', 'd']
    
    for i in range(len(my_list) - 1):
        dictionary[my_list[i]] = (my_list[i], )
    
    for i in sorted(dictionary.keys()):
        k = dictionary[i]
        print(k[0])
    

    
    
def is_prime(num: int) -> bool:
    if num <2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def is_prime_effective(n): # is 2 times faster than the previos because it requires much less operations due to loop optimization (avoided even numbers check)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(122))
    print(is_prime(7))
    print(is_prime_effective(155))
    print(is_prime_effective(353))


            
    