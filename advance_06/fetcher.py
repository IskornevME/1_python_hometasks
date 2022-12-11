import time
import sys
import asyncio
import aiohttp
from aioresponses import aioresponses


SYMBOL = "0"


async def fetch_url(url, session, res_dict):
    async with session.get(url) as resp:
        data = await resp.read()
        num_zeros = data.decode('utf-8').count(SYMBOL)
        print(f"Resp status = {resp.status}.", f"Number occurances of {SYMBOL} =", num_zeros)
        res_dict[url] = num_zeros
        return num_zeros


async def worker(queue, session, res_dict):
    while True:
        url = await queue.get()
        try:
            await fetch_url(url, session, res_dict)
        finally:
            queue.task_done()


async def fetch_batch_urls(queue, num_workers, res_dict):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(worker(queue, session, res_dict))
            for _ in range(num_workers)
        ]
        await queue.join()

        for task in tasks:
            task.cancel()


async def main(file_name, num_workers, res_dict, mock_urls=None):
    if mock_urls:
        urls_queue = asyncio.Queue()
        for elem in mock_urls:
            await urls_queue.put(elem[0])

        with aioresponses() as mocked:
            for elem in mock_urls:
                mocked.get(elem[0], status=200, body=elem[1], repeat=True)

            t_1 = time.time()
            await fetch_batch_urls(urls_queue, num_workers, res_dict)
            print("Time of fetching mocked urls", time.time() - t_1)
            print(f"Number of workers {num_workers}")

    else:
        with open(file_name) as file:
            lines = file.readlines()
            n_urls = int(lines[0])
            urls_queue = asyncio.Queue()
            for i in range(1, n_urls + 1):
                await urls_queue.put(lines[i].rstrip())

            t_1 = time.time()
            await fetch_batch_urls(urls_queue, num_workers, res_dict)
            print("Time of fetching urls", time.time() - t_1)
            print(f"Number of workers {num_workers}")

if __name__ == '__main__':
    workers = int(sys.argv[1])
    filename = sys.argv[2]
    urls_dict = dict()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(filename, workers, urls_dict))
    loop.close()
