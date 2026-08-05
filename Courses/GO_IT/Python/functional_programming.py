def decor_addition(func):
    def wrapper(a, b):
        print("Before addition")
        result = func(a, b)
        print("After addition")
        return result
    return wrapper

@decor_addition
def addition(a, b):
    res = a + b
    print(f"Adding {a} and {b} will give {res}")
    return res

# Carring example
def decor_subtraction(a):
    def inner(b):
        print("Before subtraction")
        result = a - b
        print("After subtraction")
        return result
    return inner


if __name__ == "__main__":
    result = addition(5, 3)
    print(f"Result: {result}")

    # Carrying example
    subtract = decor_subtraction(10)
    result_sub = subtract(4)
    print(f"Result of subtraction: {result_sub}")

