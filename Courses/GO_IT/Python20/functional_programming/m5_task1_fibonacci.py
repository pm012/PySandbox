def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    return fibonacci

if __name__ == "__main__":
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))


"""
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

if __name__ == "__main__":
    fib = caching_fibonacci()
    n = 10
    print(f"Fibonacci of {n} is {fib(n)}")
    n = 15
    print(f"Fibonacci of {n} is {fib(n)}")

"""
