import time
import sys
import asyncio
import aiohttp


SYMBOL = "0"


async def fetch_url(url, session, res_dict):
    async with session.get(url) as resp:
        data = await resp.read()
        num_zeros = data.decode('utf-8').count(SYMBOL)
        print(f"Resp status = {resp.status}.", f"Number occurances of {SYMBOL} =", num_zeros)
        res_dict[url] = num_zeros
        return num_zeros


async def worker(queue, session, res_dict, file, file_error=None):
    while True:
        url = await queue.get()
        try:
            await fetch_url(url, session, res_dict)
        except:
            print("Incorrect url")
            if file_error:
                print("Incorrect url", file=file_error)
        finally:
            tmp = file.readline()
            if tmp.rstrip() != "":
                await queue.put(tmp.rstrip())
            queue.task_done()


async def fetch_batch_urls(queue, num_workers, res_dict, file, file_error=None):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(worker(queue, session, res_dict, file, file_error))
            for _ in range(num_workers)
        ]
        await queue.join()

        for task in tasks:
            task.cancel()


async def main(file_name, num_workers, res_dict, file_error=None):
    with open(file_name) as file:
        urls_queue = asyncio.Queue()
        for _ in range(num_workers):
            tmp = file.readline()
            await urls_queue.put(tmp.rstrip())

        t_1 = time.time()
        await fetch_batch_urls(urls_queue, num_workers, res_dict, file, file_error)
        print("Time of fetching urls", time.time() - t_1)
        print(f"Number of workers {num_workers}")


if __name__ == '__main__':
    workers = int(sys.argv[1])
    filename = sys.argv[2]
    urls_dict = dict()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(filename, workers, urls_dict))
    loop.close()
