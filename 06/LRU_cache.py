'''
In this module we make class for LRUCache without OrderedDict
'''
import collections


class LRUCache:
    '''
    This is class for LRUCache without OrderedDict
    '''
    def __init__(self, limit=2):
        self.limit = limit
        self.size = 0
        self.keys = collections.deque()
        self.values = collections.deque()

    def get(self, key):
        try:
            i = self.keys.index(key)
        except ValueError:
            return None
        tmp = self.values[i]
        del self.keys[i]
        del self.values[i]
        self.keys.append(key)
        self.values.append(tmp)
        return tmp

    def set_(self, key, value):
        self.my_remove(key)
        if self.size + 1 <= self.limit:
            self.keys.append(key)
            self.values.append(value)
            self.size += 1
        else:
            self.keys.popleft()
            self.values.popleft()
            self.keys.append(key)
            self.values.append(value)

    def my_remove(self, key):
        for i, elem in enumerate(self.keys):
            if elem == key:
                del self.keys[i]
                del self.values[i]
                self.size -= 1
                break
