x = "y"
while x == "y":
    num = int(input("Enter a number: "))
    if num > 0:
        if num % 2 != 0:
            result = "Positive odd number"
        else:
            result = "Positive even number"
    elif num < 0:
        result = "Negative number"
    else:
        result = "It is zero"
    print(result)
    x = input("Enter y to continue set any other char to quit: ")