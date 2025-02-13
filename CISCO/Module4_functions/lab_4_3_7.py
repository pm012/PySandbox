# Define if number is prime
def is_prime(num: int)-> bool:
    if num<2:
        return False
    if num in (2, 3):
        return True
    
    if num%2 ==0 or num % 3 == 0:
        return False
    
    # for i in   (5, num ** 0.5, 6):
    #     if (num % i == 0) or (num % (i+2)==0):
    #         return False 
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6  # Increment by 6 to check numbers of the form 6k ± 1
        
    return True
    
    
lst = []
res = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]

for i in range(1, 256):
    if is_prime(i + 1):
        lst.append(i+1)
        print(i + 1, end=" ")
print()

print(f" Primary numbers length: {len(lst)} Expectd primary numbers {len(res)}")

# Validation
print(f"Missing primes: {set(res) - set(lst)}")
print(f"Extra primes: {set(lst) - set(res)}")

