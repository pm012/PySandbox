def my_deco(func):
    def inner(*args, **kwargs):
        print("Some text before function call")
        res = func(*args, **kwargs)
        print("Some text after function call")
        return res
    return inner




@my_deco
def print_name(name: str)->None:
    print(name)
    return name

if __name__ == "__main__":
    print_name("Serhii")