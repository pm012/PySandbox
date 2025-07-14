'''
 Extend the Queue class's capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.

1
dog
False
Queue empty
'''

class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.queue=[]
        
        
    def put(self, elem):
        self.queue.append(elem)
        
        

    def get(self):
        if self.queue:           
            elem = self.queue[0]
            del self.queue[0]
            return elem
        else:
            raise QueueError
        

class SuperQueue(Queue):    
    
    def isempty(self):
        return len(self.queue)==0

if __name__ == "__main__":
    que = SuperQueue()
    que.put(1)
    que.put("dog")
    que.put(False)
    for i in range(4):
        if not que.isempty():
            print(que.get())
        else:
            print("Queue empty")