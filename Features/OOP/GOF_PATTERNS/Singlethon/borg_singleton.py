class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

if __name__ == "__main__":
    b1 = Borg()
    b2 = Borg()

    b1.value = 42
    print(b2.value)




