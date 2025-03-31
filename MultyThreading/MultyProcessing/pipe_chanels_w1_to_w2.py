from multiprocessing import Pipe, Process, current_process
import logging

# Setup logging
logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# Create pipes for communication
# Note the order is important with duplex=False
worker1_recv, main_send = Pipe(duplex=False)  # Main sends to Worker1
worker2_recv, worker1_send = Pipe(duplex=False)  # Worker1 sends to Worker2
main_recv, worker2_send = Pipe(duplex=False)  # Worker2 sends to Main

def worker1(recv_pipe, send_pipe):
    """ Worker-1: Receives from main, squares, sends to Worker-2 """
    name = current_process().name
    logger.debug(f"{name} started...")

    val = recv_pipe.recv()
    logger.debug(f"{name} received: {val}")

    squared = val ** 2
    send_pipe.send(squared)
    logger.debug(f"{name} sent to Worker-2: {squared}")

    recv_pipe.close()
    send_pipe.close()

def worker2(recv_pipe, send_pipe):
    """ Worker-2: Receives from Worker-1, doubles, sends to Main """
    name = current_process().name
    logger.debug(f"{name} started...")

    val = recv_pipe.recv()
    logger.debug(f"{name} received from Worker-1: {val}")

    doubled = val * 2
    send_pipe.send(doubled)
    logger.debug(f"{name} sent to Main: {doubled}")

    recv_pipe.close()
    send_pipe.close()

if __name__ == '__main__':
    # Create workers
    w1 = Process(target=worker1, args=(worker1_recv, worker1_send), name="Worker-1")
    w2 = Process(target=worker2, args=(worker2_recv, worker2_send), name="Worker-2")

    w1.start()
    w2.start()

    # Main sends to Worker1
    main_send.send(5)
    logger.debug("Main sent 5 to Worker-1")
    main_send.close()  # Close after sending

    # Main receives from Worker2
    result = main_recv.recv()
    logger.debug(f"Main process received final result: {result}")
    main_recv.close()

    # Clean up
    w1.join()
    w2.join()