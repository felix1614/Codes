import websockets
import asyncio


async def listen():
    url = "ws://0.0.0.0:7000"

    async with websockets.connect(url) as ws:
        await ws.send("hello boyyy")
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())