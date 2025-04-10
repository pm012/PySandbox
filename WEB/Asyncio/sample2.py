from concurrent.futures import ThreadPoolExecutor
from time import sleep, time
import asyncio

fake_users = [
    {'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'},
    {'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'},
    {'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller', 'email': 'alancoleman@example.net'}
]

# without async
def get_user_sync(uid: int) -> dict:
    sleep(0.5)
    user, = list(filter(lambda user: user["id"] == uid, fake_users))
    return user

# with async
async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    user, = list(filter(lambda user: user["id"]==uid, fake_users))
    return user

#  sync-функції in thread
def get_user_threaded(uid: int) -> dict:
    return get_user_sync(uid)

async def main():
    r = []
    for i in range(1,4):
        r.append(get_user_async(i))
    return await asyncio.gather(*r)

# Async обгортка для виклику поточних sync-функцій у тредах
async def main_threaded():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(pool, get_user_threaded, i)
            for i in range(1, 4)
        ]
        return await asyncio.gather(*tasks)




if __name__ == '__main__':
    # whithout async
    start = time()
    for i in range(1, 4):
        print(get_user_sync(i))
    print(f"Time without async {time() - start}")
    
    # async
    start = time()
    result = asyncio.run(main())
    for r in result:
        print(r)
    print(f"Time with async {time() - start}")
    
    
    # Multithreading
    start = time()
    result = asyncio.run(main_threaded())
    for r in result:
        print(r)
    print(f"🔀 Time THREADED: {time() - start:.2f} sec\n")
    
    
