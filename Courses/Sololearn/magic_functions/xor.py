class A:
    set = {}

    def __init__(self):
        self.set = {1, 2, 3}

    # def __xor__(self, other):
    #     return self.set ^ other.set


class B:
    set = {}

    def __init__(self):
        self.set = {3, 2, 5}

    def __xor__(self, other):
        return self.set ^ other.set

    def __rxor__(self, other):
        return other.set ^ self.set


print(A() ^ B()) #will call the __rxor___ from B()
