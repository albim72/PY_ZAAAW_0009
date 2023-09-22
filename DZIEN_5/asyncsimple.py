import time
import asyncio

def count():
    print("element pierwszy")
    time.sleep(1)
    print("element drugi")

async def acount():
    print("element async pierwszy")
    await asyncio.sleep(1)
    print("element async drugi")

def main():
    for _ in range(3):
        count()
async def asmain():
    await asyncio.gather(acount(), acount(), acount())

if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f'{__file__} wykonany w {elapsed:0.2f} s.')

    print("_"*35)
    s = time.perf_counter()
    asyncio.run(asmain())
    elapsed = time.perf_counter() - s
    print(f'{__file__} wykonany asynchronicznie w {elapsed:0.2f} s.')
