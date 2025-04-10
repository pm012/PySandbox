import asyncio
from aiofile import async_open # for async file handling
from aiopath import AsyncPath
import os


async def main():
    apath = AsyncPath(file_path)
    print(f"Check if hello.txt present: {await apath.exists()}")
    print(f"Is a file: {await apath.is_file()}")
    print(f"Is dir: {await apath.is_dir()}")
    async with async_open(file_path, 'w+') as afp:
        await afp.write("Hello ")
        await afp.write("world\n")
        await afp.write("Hello from - async world!")
        
    print("##############apf.read() -read all lines########################")
    async with async_open(file_path, 'r') as afp:
        print(await afp.read())
        
    print("##############Line by line (async for)########################")
    async with async_open(file_path, 'r') as afp:        
        async for line in afp:
            print(line, end='') # can be line.strip() as well to avoid usless line gap between rows
            
    


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "hello.txt")
    print("Current working directory:", os.getcwd())
    asyncio.run(main())
