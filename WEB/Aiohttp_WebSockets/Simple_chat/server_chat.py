import asyncio
import logging
import websockets
import names
from websockets.exceptions import ConnectionClosedOK

logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()
    
    async def register(self, ws):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        
        self.clients.add(ws)
        logging.info(f"{ws.remote_address} connects")
        
    async def unregister(self, ws):
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnects")
        
    async def send_to_clients(self, message: str):
        if self.clients:
            [[await client.send(message) for client in self.clients]]
            
            
   
    async def distribute(self, ws):
        async for message in ws:
            await self.send_to_clients(f"{ws.name}: {message}")
            logging.info(f"Client {ws.name} sent message: ' {message}'")
            
    
    async def handler(self, ws):
        await self.register(ws)
        try:
            await self.distribute(ws)
        except ConnectionClosedOK:
            logging.info(f"{ws.remote_address} disconnected")
        finally:
            await self.unregister(ws)
    
    
async def main():
    server = Server()
    async with websockets.serve(server.handler, 'localhost', 9090) as mysocket:
        await asyncio.Future()
            
                    



if __name__ == "__main__":
    asyncio.run(main())
        