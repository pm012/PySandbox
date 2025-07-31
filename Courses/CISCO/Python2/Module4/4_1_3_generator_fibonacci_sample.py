def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

if __name__ == "__main__":
    fibs = list(fibonacci(10))
    print(fibs)

