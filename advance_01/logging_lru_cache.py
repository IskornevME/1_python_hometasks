"""
In this module we make logging LRUCache class
"""
import collections
import logging
import sys


class LRUCache:
    """
    This is class for LRUCache without OrderedDict
    """
    def __init__(self, limit=2):
        self.limit = limit
        self.size = 0
        self.keys = collections.deque()
        self.values = collections.deque()

        self.logger = logging.getLogger("logging_lru_cache")
        self.logger.setLevel(logging.INFO)
        formatter_file = logging.Formatter(
            "%(asctime)s - %(levelname)s - funcName: %(funcName)s - filename: %(filename)s"
            "- lineno: %(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S")
        formatter_stdout = logging.Formatter(
            "%(asctime)s\t%(levelname)s\t%(name)20s\t%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S")
        file_handler = logging.FileHandler('logging_lru_cache.log', mode="w")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter_file)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter_stdout)
        self.logger.addHandler(file_handler)
        if PARAM == 1:
            self.logger.addHandler(stream_handler)

        self.logger.info('Logging setup completed successfully')

    def get(self, key):
        try:
            i = self.keys.index(key)
        except ValueError:
            self.logger.exception("ValueError. There is not such key in dict")
            return None
        tmp = self.values[i]
        del self.keys[i]
        del self.values[i]
        self.keys.append(key)
        self.values.append(tmp)
        self.logger.info("Move element with key = %s to the top", key)
        return tmp

    def set_(self, key, value):
        self.my_remove(key)
        if self.size + 1 <= self.limit:
            self.keys.append(key)
            self.values.append(value)
            self.size += 1
            self.logger.info("Successfully added new element. Size has increased by one."
                             "Now size = %s", self.size)
        else:
            self.keys.popleft()
            self.values.popleft()
            self.logger.info("Delete the oldest key and value")
            self.logger.info("Successfully added new element. Size hasn't change")
            self.keys.append(key)
            self.values.append(value)

    def my_remove(self, key):
        for i, elem in enumerate(self.keys):
            if elem == key:
                self.logger.warning("Key = %s already exist. Let's rewrite its value.", key)
                del self.keys[i]
                del self.values[i]
                self.size -= 1
                break


PARAM = 0
if len(sys.argv) == 1:
    PARAM = 0
elif len(sys.argv) == 2 and sys.argv[1] == "-s":
    PARAM = 1
else:
    print("If you want logging in file don't print"
          " any arguments. If you also want logging to stdout"
          " print '-s'.")
    sys.exit(1)

cache = LRUCache()
cache.set_('k1', 'val1')
cache.set_('k2', 'val2')
cache.get('k3')
cache.set_('k3', 'val3')
cache.set_('k3', '777')
cache.get('k2')
