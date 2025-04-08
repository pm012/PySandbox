import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests
from time import time

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']


def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


async def preview_fetch_async():
    # Get the currently running asyncio event loop
    loop = asyncio.get_running_loop()

    # Create a thread pool with 3 workers
    with ThreadPoolExecutor(3) as pool:
        # Submit each `preview_fetch(url)` call to the thread pool via the event loop
        # This returns a list of awaitables
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]

        # Await all thread-based tasks concurrently
        # If any raises an exception, it'll be returned instead of raising immediately
        result = await asyncio.gather(*futures, return_exceptions=True)
        return result

if __name__ == '__main__':
    start = time()
    for url in urls:
        r = preview_fetch(url)
        print(r)
    print(f"Synchronious request: {time() - start}")
    
    start = time()
    r = asyncio.run(preview_fetch_async())
    print(r)
    print(f"Asynchronious request: {time() - start}")
    
