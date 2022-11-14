import socket
import sys
from datetime import datetime
import time
import threading
import queue
import pickle
import json


def send_urls(my_queue, client_socket):
    while True:
        try:
            url = my_queue.get()
        except queue.Empty:
            continue

        if url is None:
            print("THREAD ENDS")
            my_queue.put(None)
            break

        time.sleep(0.05)
        client_socket.send(url.encode())


def client_program():
    host = "localhost"
    port = 5033
    client_socket = socket.socket()
    client_socket.connect((host, port))

    with open(filename) as file:
        lines = file.readlines()
        amount = int(lines[0])
        my_queue = queue.Queue(maxsize=amount + 1)
        for i in range(1, amount + 1):
            my_queue.put(lines[i])

    my_queue.put(None)

    client_socket.send(bytes(str(amount), 'utf8'))

    start_time = datetime.now()

    threads = [
        threading.Thread(
            target=send_urls,
            args=(my_queue, client_socket),
        )
        for _ in range(N_THREADS_C)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(datetime.now() - start_time)

    client_socket.send(bytes(str("stop"), 'utf8'))

    all_data = bytearray()
    res = []
    while True:

        data = client_socket.recv(1024)
        if not data:
            break

        obj = pickle.loads(data)
        print(obj)
        all_data += data
        res.append(obj)

    with open("res.json", "w+") as outfile:
        json.dump(res, outfile)

    client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python client.py 10 urls.txt")
    N_THREADS_C = int(sys.argv[1])
    filename = sys.argv[2]

    client_program()
