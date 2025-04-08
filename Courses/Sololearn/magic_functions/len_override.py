import random


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        # redefined to return random item based on index
        res = index + random.randint(-1, 1)
        print(res)
        if res not in (0, len(self)):
            res = -1  # return last element
            print(f'adjusted: {res}')

        return self.cont[res]

    def __len__(self):
        return random.randint(0, len(self.cont) * 2)


vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[4])
