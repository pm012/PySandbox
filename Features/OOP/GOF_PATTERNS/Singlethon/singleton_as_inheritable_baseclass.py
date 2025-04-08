# For multiple singleton classes

class SingletonInheritBase(type):
    _instances = {}

    def __call__(cls, *args, **kwds):        
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]
    
class Singleton(metaclass = SingletonInheritBase):
    pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)