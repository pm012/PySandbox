import asyncio 
import logging
import websockets
#from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK

logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()
    
    
    async def register(self, ws):
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects')
        
    async def unregister(self, ws):
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnects")
        
    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]
            
    async def distribute(self, ws):
        async for message in ws: 
            await self.send_to_clients(message)
            
    async def ws_handler(self, ws):
        await self.register(ws)
        try:
            await self.distribute(ws)
        except ConnectionClosedOK:
            logging.info(f"{ws.remote_address} connection closed gracefully.")
        finally:
            await self.unregister(ws)
            
async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 4000):
        await asyncio.Future()
        
if __name__ == "__main__":
    asyncio.run(main())
        
    