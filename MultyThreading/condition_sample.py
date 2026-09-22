import logging
from threading import Thread, Condition
from time import sleep

def worker(condition: Condition)->None:
    logging.debug("Worker is ready to work")
    with condition:
        condition.wait()
        logging.debug("Worker can do the work")
        
def master(condition:Condition)->None:
    logging.debug("Master doing the same work")
    sleep(2)
    with condition:        
        logging.debug("Notify all workers that they can continue working")
        condition.notify_all()
        
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format = '%(threadName)s %(message)s')
    condition = Condition()
    master_thread = Thread(name="master", target=master, args=(condition,))
    worker1 = Thread(name="worker1", target=worker, args=(condition,))   
    worker2 = Thread(name="worker2", target=worker, args=(condition,))
    worker1.start()
    worker2.start()
    master_thread.start()
    
    logging.debug("End program")