import unittest


from LRU_cache import LRUCache


LIM = 2
cache = LRUCache(LIM)


class TestGet(unittest.TestCase):
    def test_index(self):
        res = cache.get('key1')
        self.assertIsNone(res)

    def test_value(self):
        cache.set_('key1', 'val1')
        res = cache.get('key1')
        self.assertEqual(res, 'val1')


class TestOrder(unittest.TestCase):
    def test_size(self):
        cache.set_('key1', 'val1')
        cache.set_('key2', 'val2')
        self.assertEqual(cache.size, LIM)
        cache.set_('key3', 'val3')
        self.assertEqual(cache.size, LIM)

    def test_order(self):
        cache.set_('key1', 'val1')
        cache.set_('key2', 'val2')
        cache.set_('key3', 'val3')
        self.assertIsNone(cache.get('key1'))
        self.assertEqual(cache.get('key2'), 'val2')
        self.assertEqual(cache.get('key3'), 'val3')

        cache.get('key2')
        cache.set_('key4', 'val4')
        self.assertIsNone(cache.get('key3'))
        self.assertEqual(cache.get('key4'), 'val4')
        self.assertEqual(cache.get('key2'), 'val2')

    def test_keys(self):
        cache.set_('key1', 'val1')
        cache.set_('key2', 'val2')
        self.assertEqual(cache.size, LIM)
        self.assertEqual(cache.get('key2'), 'val2')
        cache.set_('key2', '999')
        self.assertEqual(cache.get('key2'), '999')
        self.assertEqual(cache.size, LIM)
