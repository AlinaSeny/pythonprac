import asyncio
from time import strftime


async def snd(evsnd):
    print(f'snd : generated evsnd')
    evsnd.set()
    return 1


async def mid1(evsnd, evmid1):
    print(f'snd : generated evmid1')
    await evsnd.wait()
    print(f'rcv : generated evsnd')
    evmid1.set()
    return 2


async def mid2(evsnd, evmid2):
    print(f'snd : generated evmid2')
    await evsnd.wait()
    print(f'rcv : generated evsnd')
    evmid2.set()
    return 2


async def rcv(ev1, ev2):
    await ev1.wait()
    print(f'rcv : generated evmid1')
    await ev2.wait()
    print(f'snd : generated evmid2')
    return 3


async def main():
    ev1, ev2, ev3 = asyncio.Event(), asyncio.Event(), asyncio.Event()
    res = await asyncio.gather(
        snd(ev1),
        mid1(ev1, ev2),
        mid2(ev1, ev3),
        rcv(ev2, ev3)
    )
    print(res)

asyncio.run(main())
