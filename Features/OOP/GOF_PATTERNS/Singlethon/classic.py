class Singlethon:
    _instance = None 

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    

s1 = Singlethon()
s2 = Singlethon()

print(s1 is s2)


