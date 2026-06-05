import asyncio

# import time


async def make_tea(name):
    print(f"Making {name}...")
    await asyncio.sleep(5)
    # time.sleep(2)
    print(f"{name} is ready!")


async def main():
    await asyncio.gather(
        make_tea("tea"),
        make_tea("coffee"),
        make_tea("Milk tea"),
        make_tea("Black tea"),
    )


if __name__ == "__main__":
    asyncio.run(main())
