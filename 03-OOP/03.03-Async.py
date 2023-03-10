import asyncio
import time

'''
import random

async def async_function1():
    for i in range(5):
        print(f"Function 1: {i}")
        await asyncio.sleep(random.uniform(0.999, 1.001))

async def async_function2():
    for i in range(5):
        print(f"Function 2: {i}")
        await asyncio.sleep(random.uniform(0.999, 1.001))

async def main():
    task1 = asyncio.create_task(async_function1())
    task2 = asyncio.create_task(async_function2())

    await task1
    await task2
'''


async def func_1():
    for i in range(11):
        print(i)
        await asyncio.sleep(0.8)


async def func_2():
    print("Hello...")
    await asyncio.sleep(5)
    print("...World!")


async def main():
    print("START")
    await asyncio.gather(func_1(), func_2())
    print("FINISH")


if __name__ == "__main__":
    start_time = time.perf_counter()  # time.time()
    asyncio.run(main())
    end_time = time.perf_counter()  # time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
