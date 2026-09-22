from threading import Thread, Semaphore
from time import sleep
import logging

def worker(condition):
    with condition:
        logging.debug("started semaphore")
        sleep(2)
        logging.debug("End semaphore")
        
if __name__ == "__main__":
     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
     pool = Semaphore(2)
     for num in range(10):
         thread = Thread(name=f"Thread-{num}", target=worker, args=(pool,))
         thread.start()
         


