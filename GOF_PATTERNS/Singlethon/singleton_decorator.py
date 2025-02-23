def singleton(cls):
    instanses = {}

    def get_instance(*args, **kwargs):
        if cls not in instanses:
            instanses[cls] = cls(*args, **kwargs)
        return instanses[cls]
    
    return get_instance

@singleton
class Singleton():
    pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)
    print(s1 == s2)


