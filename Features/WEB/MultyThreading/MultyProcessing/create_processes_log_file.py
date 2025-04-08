from multiprocessing import Process, Queue
import logging
import logging.handlers
import os
from time import sleep


def setup_logger(log_queue):
    """Configure logger to send logs to a queue"""
    logger = logging.getLogger()

    while logger.hasHandlers():  # Remove old handlers
        logger.removeHandler(logger.handlers[0])

    logger.setLevel(logging.DEBUG)

    # Use QueueHandler to send logs to the main process
    queue_handler = logging.handlers.QueueHandler(log_queue)
    logger.addHandler(queue_handler)


def logger_listener(log_queue):
    """Logger process that writes logs to file"""
    logger = logging.getLogger("listener")

    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logfile.log")

    file_handler = logging.FileHandler(log_file_path, mode="a")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    while True:
        try:
            record = log_queue.get()
            if record is None:  # Stop the listener when None is received
                break
            logger.handle(record)
        except Exception:
            import traceback
            print(traceback.format_exc())


class MyProcess(Process):
    def __init__(self, log_queue, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.log_queue = log_queue

    def run(self) -> None:
        setup_logger(self.log_queue)
        logger = logging.getLogger()
        logger.debug(f"Process message: {self.args[0]}")


def example_work(params, log_queue):
    sleep(0.5)
    setup_logger(log_queue)
    logger = logging.getLogger()
    logger.debug(params)


if __name__ == "__main__":
    log_queue = Queue()

    # Start a separate process to listen and write logs
    listener = Process(target=logger_listener, args=(log_queue,))
    listener.start()

    processes = []
    for i in range(3):
        pr = Process(target=example_work, args=(f"Count process function - {i}", log_queue))
        pr.start()
        processes.append(pr)

    for i in range(2):
        pr = MyProcess(log_queue, args=(f"Count process calls - {i}",))
        pr.start()
        processes.append(pr)

    # Wait for all processes to complete
    for el in processes:
        el.join()

    # Send a stop signal to the listener
    log_queue.put(None)
    listener.join()
    [print(el.exitcode, end=' ') for el in processes]

    print("Logging complete. Check logfile.log.")
