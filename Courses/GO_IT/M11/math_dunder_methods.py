from collections import UserDict

class MyDict(UserDict):
    def __add__(self, other):
        new_dict = MyDict(self.data) # copy of self
        new_dict.update(other)
        return new_dict


    def __sub__(self, other):
        new_dict = MyDict(self.data)
        for key in new_dict:
            if key in other:
                new_dict.pop(key, None) # remove key if exists (use second parameter "None" to avoid key error)
                return new_dict




d1 = MyDict({1: 'a', 2: 'b'})
d2 = MyDict({3: 'c', 4: 'd'})


d3 = d1 + d2
print(d3)# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


d4 = d3 - d2
print(d4)# {1: 'a', 2: 'b'}
