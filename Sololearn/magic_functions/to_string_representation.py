class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self): #To string
        return "Queue({})".format(self._hiddenlist)

    @property
    def hiddenlist(self): # to use in direct call
        return self._hiddenlist


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue.hiddenlist) # to access private attribute
