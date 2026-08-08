import asyncio
import aiohttp


async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Got response for {url} with status {response.status}")
        return await response.text


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            fetch_url(session, "https://httpbin.org/delay/1"),
            fetch_url(session, "https://httpbin.org/delay/2"),
            fetch_url(session, "https://httpbin.org/delay/3"),
        )


if __name__ == "__main__":
    asyncio.run(main())
