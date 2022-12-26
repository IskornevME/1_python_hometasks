'''
This file tests program fetch urls
'''
import unittest
import asyncio
from io import StringIO
import aiohttp
from aioresponses import aioresponses

import fetcher


SYMBOL = "0"


class TestFetcher(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.mock_artefacts = []
        with open("mock_artefacts.txt") as file:
            lines = file.readlines()
            for line in lines:
                self.mock_artefacts.append(list(line.split(": ")))
        with open("test_urls.txt", "w+") as test_file:
            for elem in self.mock_artefacts:
                test_file.writelines(str(elem[0]) + "\n")
        self.filename = "test_urls.txt"

    async def test_fetcher_1_work(self):
        with aioresponses() as mocked:
            for elem in self.mock_artefacts:
                mocked.get(elem[0], status=200, body=elem[1], repeat=True)
            workers = 1
            urls_dict = dict()
            await fetcher.main(self.filename, workers, urls_dict)
            get_res = []
            true_res = []
            for elem in self.mock_artefacts:
                get_res.append(urls_dict[elem[0]])
                true_res.append(elem[1].count(SYMBOL))
            self.assertListEqual(true_res, get_res)

    async def test_worker(self):
        with open("test_urls.txt", "r+") as test_file:
            with aioresponses() as mocked:
                urls_queue = asyncio.Queue()
                for elem in self.mock_artefacts:
                    mocked.get(elem[0], status=200, body=elem[1], repeat=True)
                res_dict = dict()
                num_workers = 2
                for _ in range(num_workers):
                    tmp = test_file.readline()
                    await urls_queue.put(tmp.rstrip())
                async with aiohttp.ClientSession() as session:
                    tasks = [
                        asyncio.create_task(
                            fetcher.worker(urls_queue, session, res_dict, test_file)
                        )
                        for _ in range(num_workers)
                    ]
                    await urls_queue.join()

                    for task in tasks:
                        task.cancel()
                get_res = []
                true_res = []
                for elem in self.mock_artefacts:
                    get_res.append(res_dict[elem[0]])
                    true_res.append(elem[1].count(SYMBOL))
                self.assertListEqual(true_res, get_res)

    async def test_worker_exception(self):
        excep_url = "https://incorrect_url_324edfewrr4"
        with open("test_urls.txt", mode="a") as test_file:
            test_file.writelines(excep_url + "\n")
        self.mock_artefacts.append([excep_url, "df0sc"])
        with open("test_urls.txt", "r+") as test_file:
            with aioresponses() as mocked:
                urls_queue = asyncio.Queue()
                for elem in self.mock_artefacts:
                    if elem[0] != excep_url:
                        mocked.get(elem[0], status=200, body=elem[1], repeat=True)
                res_dict = dict()
                file_for_error = StringIO()

                num_workers = 1
                for _ in range(num_workers):
                    tmp = test_file.readline()
                    await urls_queue.put(tmp.rstrip())
                async with aiohttp.ClientSession() as session:
                    tasks = [
                        asyncio.create_task(
                            fetcher.worker(urls_queue, session, res_dict, test_file, file_for_error)
                        )
                        for _ in range(num_workers)
                    ]
                    await urls_queue.join()
                    for task in tasks:
                        task.cancel()
                self.assertRaises(KeyError, lambda: res_dict[excep_url])
                self.assertEqual(file_for_error.getvalue().rstrip(), "Incorrect url")

    async def test_fetch_url(self):
        with aioresponses() as mocked:
            urls = [
                ["http://example_1", "fe000rw0"],
                ["http://example_2", " "],
                ["http://example_3", "0 0000 w0"]
                    ]
            for elem in urls:
                mocked.get(elem[0], status=200, body=elem[1], repeat=True)
            res_dict = dict()
            res_arr = []
            async with aiohttp.ClientSession() as session:
                for elem in urls:
                    tmp = await fetcher.fetch_url(elem[0], session, res_dict)
                    res_arr.append(tmp)
            expected_dict = {
                'http://example_1': 4,
                'http://example_2': 0,
                'http://example_3': 6
            }
            self.assertListEqual(res_arr, [4, 0, 6])
            self.assertDictEqual(res_dict, expected_dict)

    async def test_fetcher_20_work(self):
        with aioresponses() as mocked:
            for elem in self.mock_artefacts:
                mocked.get(elem[0], status=200, body=elem[1], repeat=True)
            workers = 20
            urls_dict = dict()
            await fetcher.main(self.filename, workers, urls_dict)
            get_res = []
            true_res = []
            for elem in self.mock_artefacts:
                get_res.append(urls_dict[elem[0]])
                true_res.append(elem[1].count(SYMBOL))
            self.assertListEqual(true_res, get_res)
