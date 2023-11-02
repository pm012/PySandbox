def gcd():
    # greatest common divisor
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))

    gcd = first if first <= second else second
    while (first % gcd != 0) or (second % gcd != 0):
        gcd -= 1

    print(gcd)


def reversed_loop():
    # reversed for loop
    for i in reversed(range(101)):
        print(i)


def nested_loops():
    # nested loop without break
    num = int(input("Enter integer (0 for output): "))
    sum = 0
    while num != 0:
        for e in range(num, -1, -1):
            sum += e

        num = int(input("Enter integer (0 for output): "))
    print(sum)


def nested_loops_break():
    # nested loop with break
    sum = 0
    while True:
        num = int(input("Enter integer (0 for output): "))
        if num == 0:
            break
        for e in range(num, -1, -1):
            sum += e

    print(sum)


def nested_loops_continue():
    sum = 0
    while True:
        num = int(input("Enter integer (0 for output): "))
        if num == 0:
            break
        for i in range(num + 1):
            if i % 2 != 0:
                continue
            sum += i
    print(sum)


def cesarius_cipher():
    message = input("Enter a message: ")
    offset = int(input("Enter the offset: "))
    encoded_message = ""
    for ch in message:
        if ch.isalpha():
            if ch.islower():
                pos = ord(ch) - ord('a')
                pos = (pos + offset) % 26
                new_char = chr(pos + ord('a'))
                encoded_message += new_char
            elif ch.isupper():
                pos = ord(ch) - ord('A')
                pos = (pos + offset) % 26
                new_char = chr(pos + ord('A'))
                encoded_message += new_char
        else:
            encoded_message += ch
    print(encoded_message)


def div_zr_exception():
    pool = 1000
    quantity = int(input("Enter the number of mailings: "))
    try:
        chunk = pool // quantity
    except ZeroDivisionError:
        print('Divide by zero completed!')
    else:
        print(chunk)


# nested_loops_break()
# nested_loops_continue()
# cesarius_cipher()
div_zr_exception()
