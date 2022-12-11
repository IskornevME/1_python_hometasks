'''
This file tests program fetch urls
'''
import unittest
import asyncio

import fetcher


SYMBOL = "0"
FILENAME = "urls.txt"


class TestFetcher(unittest.TestCase):
    def setUp(self):
        self.mock_artefacts = []
        with open("mock_artefacts.txt") as file:
            lines = file.readlines()
            for line in lines:
                self.mock_artefacts.append(list(line.split(": ")))

    def test_urls_1_worker(self):
        workers = 10
        urls_dict = dict()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(fetcher.main(FILENAME, workers, urls_dict, self.mock_artefacts))
        get_res = []
        true_res = []
        for elem in self.mock_artefacts:
            get_res.append(urls_dict[elem[0]])
            true_res.append(elem[1].count(SYMBOL))
        self.assertListEqual(true_res, get_res)

    def test_urls_20_worker(self):
        print()
        workers = 20
        urls_dict = dict()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(fetcher.main(FILENAME, workers, urls_dict, self.mock_artefacts))
        loop.close()
        get_res = []
        true_res = []
        for elem in self.mock_artefacts:
            get_res.append(urls_dict[elem[0]])
            true_res.append(elem[1].count(SYMBOL))
        self.assertListEqual(true_res, get_res)
