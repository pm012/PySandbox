import asyncio
import websockets

# Open the client.html file in browser and click the button
async def handler(websocket):
    data = await websocket.recv()
    reply = f"Data received as {data}!"
    print(reply)
    await websocket.send(reply)

async def main():
    async with websockets.serve(handler, "localhost", 8000):
        await asyncio.Future() # run forever

if __name__ == "__main__":
    asyncio.run(main())