"""
One of the classic recursion problems that is often asked at interviews, especially for 
beginner programmers, is the Fibonacci series.

A Fibonacci series is a sequence of numbers of the form: 0, 1, 1, 2, 3, 5, 8, ... where each subsequent number 
in the sequence is obtained by adding the two previous members of the series.

In general, to calculate the nth term of the Fibonacci series, you should calculate the expression:

Fn = Fn-1 + Fn-2

This task can be solved recursively by calling a function that calculates the sequence numbers 
until the call reaches the terms of the series less than n = 1, where the sequence is given.
"""

def fib(n: int)-> int:
    if n in (0, 1):        
        return n    
    res = fib(n-1) + fib(n-2)    
    return res

if __name__ == "__main__":
    n = int(input("Enter the fibonacci number to get secuence:"))
    sequence = [fib(i) for i in range (n-1)]
    print(sequence)

