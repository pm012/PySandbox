def decor(func):
    def wrap():
        print("=================")
        func()
        print("+++++++++++++++++++")

    return wrap


@decor
def print_text():
    print("Hello world!")


print_text()

#or if without @decor it should be following call:
decorated = decor(print_text)
decorated()
