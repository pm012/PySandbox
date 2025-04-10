import asyncio
import concurrent.futures
from time import time

# Returns time it took to finish cpu bound emulated "heavy" task
def blocks(n):
    counter = n
    start = time()
    while counter > 0:
        counter -= 1
    return time() - start


# prints time each 2 seconds (perioudic courutine). Terminated with main
async def monitoring():
    while True:
        await asyncio.sleep(2)
        print(f'Monitoring {time()}') 


async def run_blocking_tasks(executor, n):
    loop = asyncio.get_event_loop()
    print('waiting for executor tasks')
    # executes synchronous function blocks using created coroutine
    result = await loop.run_in_executor(executor, blocks, n) 
    return result 


async def main():
    #start monitoring as background task. Monitoring never awaited
    asyncio.create_task(monitoring()) 
    # creates thread pool with 3 workers ( only 3 workers needed, in case of scrapping it can be increased up t0 10-20+)
    #if we decrease the number to 2, 1 task will be idle and will wait till the other 2 end working
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: 
        #created list of three async coroutines, each of which will offload a blocks(n) call to the pool
        futures = [run_blocking_tasks(executor, n) for n in [50_000_000, 60_000_000, 70_000_000]] 
         # unpacks futures list (list of courutines) and starts them in paralel
        results = await asyncio.gather(*futures)
        # returns started courutines result of work (returns float values  returned by each blocks(n))
        return results 


if __name__ == '__main__':
    result = asyncio.run(main())
    for r in result:
        print(r)

