# import time
# import asyncio

# async def a(num):
#     await asyncio.sleep(num)
#     print(1)

# async def b(num):
#     await asyncio.sleep(num)
#     print(2)

# async def main():
#     task_1 = asyncio.create_task(a())
#     task_2 = asyncio.create_task(b())

#     await task_1
#     await task_2    

# asyncio.run(main())


# import time
# import asyncio
# import random

# delays = [1, 2, 3, 4, 5]

# async def a(num):
#     await asyncio.sleep(num)
#     print(1)

# async def b(num):
#     await asyncio.sleep(num)
#     print(2)

# async def main():
#     num_a = random.choice(delays)
#     num_b = random.choice(delays)

#     task_1 = asyncio.create_task(a(num_a))
#     task_2 = asyncio.create_task(b(num_b))

#     await asyncio.gather(task_1, task_2)

# asyncio.run(main())

# import time
# import asyncio
# import random

# delays = [1, 2, 3, 4, 5]

# async def a(num):
#     await asyncio.sleep(num)
#     print(1)

# async def b(num):
#     await asyncio.sleep(num)
#     print(2)

# async def main():
#     sampled_delays = random.sample(delays, 2)
#     num_a, num_b = sampled_delays

#     task_1 = asyncio.create_task(a(num_a))
#     task_2 = asyncio.create_task(b(num_b))

#     await asyncio.gather(task_1, task_2)

# asyncio.run(main())

import time
import asyncio
import random

async def a(b):
    await asyncio.sleep(b)
    print(1)

async def b(a):
    await asyncio.sleep(a)
    print(2)

async def main():
    task_1 = asyncio.create_task(a(random.randint(1,10)))
    task_2 = asyncio.create_task(b(random.randint(1,10)))

    await task_1
    await task_2    

# asyncio.run(main())
    
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()    

