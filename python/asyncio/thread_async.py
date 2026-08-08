import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def check_stock(item):
    print(f"Checking stock for {item}")
    time.sleep(2)
    return f"{item} is in stock"


async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            check_stock,
            "coffee",
        )

        print(result)


asyncio.run(main())
