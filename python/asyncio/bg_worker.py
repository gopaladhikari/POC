import asyncio
import threading
import time


def background_worker():
    while True:
        time.sleep(3)
        print("I'm a background worker")


async def fetch_data():
    await asyncio.sleep(1)
    print("Fetched data")


thread = threading.Thread(target=background_worker, daemon=True)

thread.start()


asyncio.run(fetch_data())
