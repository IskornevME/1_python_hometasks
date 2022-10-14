'''
This file tests the lru_cache
'''
import unittest
from lru_cache import LRUCache


class TestGet(unittest.TestCase):
    '''
    Test that we can access an element by its key
    '''
    def test_index(self):
        cache = LRUCache()
        res = cache.get('key1')
        self.assertIsNone(res)

    def test_value(self):
        cache = LRUCache()
        cache.set_('key1', 'val1')
        res = cache.get('key1')
        self.assertEqual(res, 'val1')


class TestOrder(unittest.TestCase):
    def test_size(self):
        '''
        Test that size of our Cache not greater than limit
        '''
        cache = LRUCache()
        cache.set_('key1', 'val1')
        cache.set_('key2', 'val2')
        self.assertEqual(cache.size, cache.limit)
        cache.set_('key3', 'val3')
        self.assertEqual(cache.size, cache.limit)

    def test_order(self):
        cache = LRUCache()
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
        '''
        Test that we can change value by existing key
        '''
        cache = LRUCache()
        cache.set_('key1', 'val1')
        cache.set_('key2', 'val2')
        self.assertEqual(cache.size, 2)
        self.assertEqual(cache.get('key2'), 'val2')
        cache.set_('key2', '999')
        self.assertEqual(cache.get('key2'), '999')
        self.assertEqual(cache.size, 2)
        cache.set_('key1', 'new_val1')
        self.assertNotEqual(cache.get('key1'), 'val1')
        self.assertEqual(cache.get('key1'), 'new_val1')
        self.assertEqual(cache.size, 2)

    def test_in_task(self):
        '''
        Check that tests from lecture is working
        '''
        cache = LRUCache()
        cache.set_('k1', 'val1')
        cache.set_('k2', 'val2')
        self.assertEqual(cache.get('k3'), None)
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertEqual(cache.get('k1'), 'val1')
        cache.set_('k3', 'val3')
        self.assertEqual(cache.get('k3'), 'val3')
        self.assertEqual(cache.get('k2'), None)
        self.assertEqual(cache.get('k1'), 'val1')

    def test_limit_eq_one(self):
        '''
        Check case than limit = 1
        '''
        cache = LRUCache(1)
        self.assertEqual(cache.limit, 1)
        self.assertEqual(cache.size, 0)
        cache.set_('k1', 'val1')
        self.assertEqual(cache.limit, 1)
        self.assertEqual(cache.size, 1)
        cache.set_('k2', 'val2')
        self.assertEqual(cache.limit, 1)
        self.assertEqual(cache.size, 1)

    def test_full_displacement(self):
        '''
        Test with complete displacement of elements
        '''
        cache = LRUCache()
        cache.set_('k1', 'val1')
        cache.set_('k2', 'val2')
        self.assertEqual(cache.size, 2)
        cache.set_('k3', 'val3')
        cache.set_('k4', 'val4')
        cache.set_('k5', 'val5')
        self.assertEqual(cache.size, 2)
        self.assertEqual(cache.get('k3'), None)
        self.assertEqual(cache.get('k4'), 'val4')
        self.assertEqual(cache.get('k5'), 'val5')
