import threading


class Singleton:
    _instance = None
    _lock = threading.Lock() # Lock for thread safety

    def __new__(cls, *args, **kwargs):
        with cls._lock: #Ensure only one thread initializes the instance
            if cls._instance is None:
                cls._instance = super().__new__(cls)

        return cls._instance
    
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)