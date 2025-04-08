#tight control and metaclass-based enforcement of singleton
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class MyClass(metaclass=SingletonMeta):
    def __init__(self):
        print('Creating MyClass')

if __name__ == '__main__':
    d1 = MyClass()
    d2 = MyClass()
    print(d1==d2)
    print(d1 is d2)


