# -------------------------------------
# asyncio.gather()
# -------------------------------------


# import asyncio

# async def download(url):
#     print(f"Downloading {url}")
#     await asyncio.sleep(2)
#     print(f"Finished {url}")

# async def main():
#     await download("site1.com")
#     await download("site2.com")

# asyncio.run(main())




# async def main():
#     await asyncio.gather(
#         download("site1.com"),
#         download("site2.com")
#     )

# asyncio.run(main())



# -------------------------------------
# aiohttp for HTTP requests
# -------------------------------------


# import aiohttp
# import asyncio

# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()

# async def main():
#     urls = ["https://api.github.com", "https://jsonplaceholder.typicode.com/posts"]
#     results = await asyncio.gather(*(fetch(url) for url in urls))
#     for content in results:
#         print(content[:100])

# asyncio.run(main())



# -------------------------------------
# Reusable sessions
# -------------------------------------


# import aiohttp
# import asyncio


# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()


# async def fetch_all(urls):
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch_with_session(session, url) for url in urls]
#         return await asyncio.gather(*tasks)


# async def fetch_with_session(session, url):
#     async with session.get(url) as response:
#         return await response.text()


# async def main():
#     urls = ["https://api.github.com", "https://jsonplaceholder.typicode.com/posts"]
#     results = await asyncio.gather(*(fetch(url) for url in urls))
#     for content in results:
#         print(content)

# asyncio.run(main())



# -------------------------------------
# Bloklovchi (blocking) 
# -------------------------------------



# import time
# import aiofiles
# import asyncio


# async def wait():
#     print('waiting start')
#     time.sleep(5)  # bloklaydi!
#     print('waiting end')


# async def wait():
#     print('waiting start')
#     await asyncio.sleep(5)  # asinxron kutish
#     print('waiting end')


# async def main():
#     await asyncio.gather(
#         wait(),
#         wait()
#     )

# asyncio.run(main())



# -------------------------------------


# import asyncio
# import time
# import aiofiles



# async def bad_read_file(path):
#     print("[BAD] Starting blocking read...")
#     with open(path, mode='r') as f:
#         f.read(1_000_000_000)
#     print("[BAD] Done reading file")



# async def good_read_file(path):
#     print("[GOOD] Starting async read...")
#     async with aiofiles.open(path, mode='r') as f:
#         await f.read(1_000_000_000)
#     print("[GOOD] Done reading file")


# async def tick():
#     for i in range(5):
#         print(f"[TICK] {i}")
#         await asyncio.sleep(0.5)


# async def main():
#     print("=== BLOCKING VERSION ===")
#     start = time.time()
#     await asyncio.gather(
#         bad_read_file("test/text.txt"),
#         tick()
#     )
#     print(f"Blocking time: {time.time() - start:.2f}s\n")

#     print("=== NON-BLOCKING VERSION ===")
#     start = time.time()
#     await asyncio.gather(
#         good_read_file("test/text_2.txt"),
#         tick()
#     )
#     print(f"Non-blocking time: {time.time() - start:.2f}s")


# if __name__ == "__main__":
#     asyncio.run(main())



# -------------------------------------
# Asynchronous context managers
# -------------------------------------


# import time
# import asyncio


# class Timer:
#     async def __aenter__(self):
#         self.start = time.perf_counter()
#         return self

#     async def __aexit__(self, exc_type, exc, tb):
#         elapsed = time.perf_counter() - self.start
#         print(f"✅ Asinxron ish {elapsed:.2f} sekundda tugadi.")

# async def some_task():
#     await asyncio.sleep(1.5)

# async def main():
#     async with Timer():
#         await some_task()

# asyncio.run(main())

