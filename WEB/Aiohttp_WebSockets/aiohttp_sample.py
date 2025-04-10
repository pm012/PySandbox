import platform

import aiohttp
import asyncio

async def python_org_request_manual_session():
    session = aiohttp.ClientSession()
    response = await session.get('https://python.org')

    print("__start inside python.org manual session__")
    print("Status:", response.status)
    print("Content-type:", response.headers['content-type'])
    html = await response.text()
    response.close() #close response
    await session.close() # close session
    print("Body:", html[:15], "...")
    print("__end of inside python.org manual session__")
    return f"Body: {html[:15]}"


async def python_org_request():
     async with aiohttp.ClientSession() as session:
        async with session.get('https://python.org') as response:

            print("__start inside python.org__")
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
            print("__end of inside python.org__")
            
async def pb_api_request():
     async with aiohttp.ClientSession() as session:
        async with session.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5') as response:
            print("__start inside privatbank___")
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            print('Cookies: ', response.cookies)
            print(response.ok)
            print("__end of inside privatbank___")
            result = await response.json()
            return result



async def main():
    print("from python.org")
    await python_org_request()
    await python_org_request_manual_session()
    print("from privatbank")
    return  await pb_api_request()
    
    

   

if __name__ == "__main__":
    # Will run only on Windows machine
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)
