def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}


def get_handler(operator):
    return OPERATIONS[operator]


handler = get_handler('-')
handler(2, 3)           # -1

get_handler('+')(2, 3)  # 5
