import socket
import pickle
import sys
import threading
from datetime import datetime
import queue
from string import ascii_letters, whitespace
from collections import Counter
import requests
from bs4 import BeautifulSoup


N_THREADS = 6


def clean(text, junk_chars):
    return text.encode('ascii', 'ignore').translate(None, junk_chars).decode()


def process_url(my_queue, conn, lock, amount):
    global JOBS_FINISHED

    while True:
        try:
            url = my_queue.get()
        except queue.Empty:
            continue

        if url is None:
            print("THREAD ENDS")
            my_queue.put(None)
            break

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        good_chars = (ascii_letters + whitespace).encode()
        junk_chars = bytearray(set(range(0x100)) - set(good_chars))

        lock.acquire()

        temp = JOBS_FINISHED
        temp += 1

        text = clean(soup.get_text(" ", strip=True), junk_chars)

        arr_words = text.split()
        #
        dct = {}
        # print(dct)
        #
        for word in arr_words:
            if word not in dct.keys():
                dct[word] = 1
            else:
                dct[word] += 1

        tmp_dict = dict(Counter(dct).most_common(TOP_K))
        data = pickle.dumps((url, tmp_dict))
        conn.send(data)

        JOBS_FINISHED = temp

        lock.release()

        print(f"{JOBS_FINISHED} \ {amount}")


def server_program():
    host = "localhost"
    port = 5033
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)

    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        all_data = bytearray()
        amount = conn.recv(4)
        amount = str(amount, 'utf8')
        amount = int(amount)
        my_queue = queue.Queue(maxsize=amount + 10)
        while True:
            data = conn.recv(1024)
            if data == bytes(str("stop"), 'utf8'):
                break

            tmp_urls = data.decode().split("\n")
            for url in tmp_urls:
                if url == "":
                    continue
                # print(tmp_urls[i])
                my_queue.put(url)

            all_data += data + " ".encode()

        # urls = all_data.decode().split()
        my_queue.put(None)

        lock = threading.Lock()

        start_time = datetime.now()

        threads = [
            threading.Thread(
                target=process_url,
                args=(my_queue, conn, lock, amount),
            )
            for _ in range(N_THREADS_S)
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print(datetime.now() - start_time)

        expected = amount

        print(f"{JOBS_FINISHED=}, {expected=}")

        conn.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("python server.py -w 10 -k 7")
    N_THREADS_S = int(sys.argv[2])
    TOP_K = int(sys.argv[4])

    JOBS_FINISHED = 0
    server_program()
