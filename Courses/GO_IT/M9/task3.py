'''
The example of caching function values can well explain the concept of closure.

The final task of Module 3 was the recursive calculation of Fibonacci numbers.

A Fibonacci series is a sequence of numbers of the form: 0, 1, 1, 2, 3, 5, 8, ..., where each subsequent number in the sequence 
is obtained by adding the two previous elements of the series.

In general, to calculate the n-th element of the Fibonacci series, you need to calculate the expression: Fn = Fn-1 + Fn-2.

This problem can be solved recursively by calling a function that calculates the sequence numbers until the call reaches
the elements of the series less than n = 1, where the sequence is given.

Create a caching_fibonacci() function that will have a cache with previously calculated Fibonacci number values. Inside is the fibonacci(n) 
function, which will directly calculate the Fibonacci number itself. The caching_fibonacci() function returns the fibonacci function.

If the Fibonacci number is stored in the cache dictionary, the fibonacci function returns the number from the cache. If it is not in the cache, 
we calculate the number, put it in the cache, and return it from the fibonacci function.

'''

def caching_fibonacci():
    cache = {0:0, 1:1}
    def fibonacci(n: int)->dict:
        if n in cache:
            return cache[n]
        cache[n]  = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci