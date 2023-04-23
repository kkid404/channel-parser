from utils import ChannelParser 
import asyncio
from loader import client
import logging
from data import ChannelService

async def main():
    logging.basicConfig(level=logging.ERROR, filename="log.txt")
    if not client.is_connected():
        await client.connect()
    channel_parser = ChannelParser()
    async with client:
        loop = asyncio.get_event_loop() # получаем текущий цикл событий
        await loop.create_task(channel_parser.set_name()) # запускаем задачу в этом цикле


if __name__ == "__main__":
    asyncio.run(main())
