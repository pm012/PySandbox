def fibonacci_loop(n):
    if n<1:
        return None
    if n in (1, 2):
        return 1
    
    el1 = el2 = 1
    sum = 0
    
    for i in range(3, n+1):
        sum = el1 + el2
        el1, el2 = el2, sum
    return sum 

def fibonacci_recursion(n):
    if n < 1: 
        return None
    if n in (1,2):
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

if __name__ == "__main__":
    for n in range(1, 11):
        print(n, "->", fibonacci_loop(n))
    print("Recursion: ")
    for n in range(1, 11):
        print(n, "->", fibonacci_recursion(n))
    