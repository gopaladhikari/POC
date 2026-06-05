import asyncio


async def make_tea():
    print("Making tea...")
    await asyncio.sleep(2)
    print("Making tea... done")


asyncio.run(make_tea())
