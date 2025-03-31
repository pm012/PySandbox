from multiprocessing import Process, Value, RLock, current_process
from time import sleep
from multiprocessing.sharedctypes import Synchronized

import logging
import sys

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def worker(val: Synchronized):
    logger.debug(f'Started {current_process().name}')
    sleep(1)
    with val.get_lock():
        val.value += 1
    logger.debug(f"Done {current_process().name}")
    sys.exit(0)
    
if __name__ == "__main__":
    lock = RLock()
    value = Value('d', 0, lock=lock)
    pr1 = Process(target=worker, args=(value, ))
    print("initalized process1")
    pr1.start()
    print("started process1")
    pr2 = Process(target=worker, args=(value, ))
    
    pr2.start()
    
    pr1.join()
    pr2.join()
    
    print(value.value)
    