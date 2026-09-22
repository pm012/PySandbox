def my_function(a,b):
    global x
    x = a+b
    return x*2

x=5
print(my_function(x, 10))
print(x)

