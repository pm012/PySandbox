from multiprocessing import RLock, current_process, Process
from multiprocessing.sharedctypes import Value, Array, Synchronized
from ctypes import Structure, c_double
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


class Pont(Structure):
    _fields_ = [('x', c_double),('y', c_double)]
    
def worker_modify(num: Synchronized, string: Array, arr: Array):
    logger.debug(f"Started {current_process().name}")
    logger.debug(f"Change num: {num.value}")
    
    with num.get_lock():
        num.value **=2 # 1. What does it mean?
        
    logger.debug(f"to num: {num.value}")
    with string.get_lock():
        string.value = string.value.upper()  # Convert to uppercase

    with arr.get_lock():
        for a in arr:
            a.x **=2 # same as 1?
            a.y **=2 # same as 1?
    logger.debug(f'Done {current_process().name}')
    
if __name__ == "__main__":
    lock = RLock()
    number = Value(c_double, 1.5, lock=lock) # 2. Can we create value as Value(c_double, 1.5, lock=RLock())? Or the lock for share value should be the same for all processes?
    string = Array('c', b'Hello world', lock=lock) # same as 2?
    array = Array(Pont, [(1, -6), (-5,2), (2, 9)], lock=lock) #  3. First parameter is array's datatype, second paraeters to pass to constructor? If yes where can we see that it is 2 integers?
    
    p1 = Process(target=worker_modify, args=(number, string, array))
    p2 = Process(target=worker_modify, args=(number, string, array))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(number.value)
    print(string.value)
    print([(arr.x, arr.y) for arr in array]) #4. Is everything in print statements get values changed by 2 processes?

