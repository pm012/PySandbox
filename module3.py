def get_fullname(first_name, last_name, middle_name=None):
    if middle_name is None:
        return f"{first_name} {last_name}"
    else:
        return f"{first_name} {middle_name} {last_name}"


s = get_fullname('Petro', 'Zaliznyak')


def make_article(title, *topics):
    print(topics)
    print(len(topics))
    return len(topics)


def make_comments(title, **comments):
    # comments hash set key->parameter_name: value
    print(comments)


def modeling(factor, *numbers, correction):
    result = 0
    for number in numbers:
        result += number + factor
    result = result + factor
    result = result + correction
    return result


def cost_delivery(quantity, *others, discount=0):
    # first element fo quantity = 5 USD and all next are
    # 2 USD each, then undefined number of parameters and not required discount (0 by default)
    price = 0
    if quantity >= 1:
        price = 5
        for e in range(1, quantity):
            price += 2
        if discount > 0:
            price *= discount

    return price


def factorial(n: int) -> int:
    # Factorial with limitation
    if n == 0:
        return 1
    return n * factorial(n - 1)


def number_of_groups(n, k):
    # combinations of groups
    return int(factorial(n) / (factorial(n - k) * factorial(k)))

def fibonacci(n):
    #fibonacci
    if n in (0, 1):
        #print(n)
        return n
    res = fibonacci(n-1) + fibonacci(n-2)
    return res


# make_article("Title", "first", "second", "third")
#make_comments("TTL", comment_one="first", comment_two="second")
# print(cost_delivery(2, 1, 2, 3))
# print(cost_delivery(3, 3))
# print(cost_delivery(1))
# print(cost_delivery(2, 1, 2, 3, discount=0.5))
