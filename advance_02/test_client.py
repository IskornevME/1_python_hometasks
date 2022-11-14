'''
This file tests client
'''
import queue
import unittest
import json
from collections import Counter
from string import ascii_letters, whitespace
from bs4 import BeautifulSoup
import requests


def clean(text, junk_chars):
    return text.encode('ascii', 'ignore').translate(None, junk_chars).decode()


def process_url(my_queue, top_k):
    ans = []
    while True:
        try:
            url = my_queue.get()
        except queue.Empty:
            continue

        if url is None:
            my_queue.put(None)
            break

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        good_chars = (ascii_letters + whitespace).encode()
        junk_chars = bytearray(set(range(0x100)) - set(good_chars))

        text = clean(soup.get_text(" ", strip=True), junk_chars)

        arr_words = text.split()
        dct = {}

        for word in arr_words:
            if word not in dct.keys():
                dct[word] = 1
            else:
                dct[word] += 1

        tmp_dict = dict(Counter(dct).most_common(top_k))
        ans.append([url, tmp_dict])
    return ans


class TestClient(unittest.TestCase):
    def test_client_server(self):
        with open("res.json", "r+") as outfile:
            res = json.load(outfile)
        res_trunc = res[0:5]
        my_queue = queue.Queue()
        arr_urls = []
        for i in range(5):
            arr_urls.append(res[i][0])
            my_queue.put(res[i][0])

        top_k = 7
        my_queue.put(None)
        res_real = process_url(my_queue, top_k)
        self.assertListEqual(res_trunc, res_real)
