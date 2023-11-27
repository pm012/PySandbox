def test(func, arg):
    return func(func(arg)) # func(func(2)) = func(mult(2)) = func(4) = mult(4)=16


def mult(x):
    return x * x


print(test(mult, 2))
