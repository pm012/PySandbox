from multiprocessing import Pool, current_process
import logging
import os

logger = logging.getLogger()
stream_hendler = logging.StreamHandler()
logger.addHandler(stream_hendler)
logger.setLevel(logging.DEBUG)

def worker (x:int)->int:
    logger.debug(f"pid = {current_process().pid}, x={x}")
    return x*x


if __name__ == "__main__":
    with Pool(processes=2) as pool: #bad practice - shuld not be hardcoded as in example
        logger.debug(pool.map(worker, range(30)))
    
    print(os.cpu_count())
        
# Ideally it should be defined the number of CPU cores to work more eficcient
# 
# import os
# with Pool(processes=os.cpu_count()) as pool:  # Uses all available CPU cores
