import logging
import asyncio
import websockets

logging.basicConfig(level= logging.INFO)


async def consumer(hostname: str, port: int):
    we_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(we_resource_url) as ws:
        async for message in ws:
            logging.info(f"Message: {message}")
            
if __name__ == "__main__":
    asyncio.run(consumer('localhost', 4000))
            
            

