import platform

import aiohttp
import asyncio
from uuid import uuid4


async def main():
    # Client timput limits how long request can take (in our case it will wait 1 sec and then raised asyncio.TimeoutError )
    timeout = aiohttp.ClientTimeout(total=1) 
    async with aiohttp.ClientSession(
        # Used internally in aiohttp.ClientSession to identify rquest and give it a unique id. Can be used in logs. uuid4 -generates unique identifier 
        headers={"Request-Id": str(uuid4())}, 
        timeout=timeout,
    ) as session:
        async with session.get('https://python.org') as response: # sends headers with the get requiest

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type']) # not sure that this is the same headers as above...

            html = await response.text()
            return f"Body: {html[:15]}..."


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)
