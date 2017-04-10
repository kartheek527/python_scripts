"""
    Unit test cases for lru cache script.
"""

__author__ = 'me@kartheek.net (Karnati Kartheek)'

import unittest
from scripts import lru_cache


class LruCacheTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_lru_cache(self):
        self.assertEqual(lru_cache.get_sqr(1), (1, 'set'))
        self.assertEqual(lru_cache.get_sqr(2), (4, 'set'))
        self.assertEqual(lru_cache.get_sqr(1), (1, 'get'))
        self.assertEqual(lru_cache.get_sqr(2), (4, 'get'))
        self.assertEqual(lru_cache.get_sqr(4), (16, 'set'))
        self.assertEqual(lru_cache.get_sqr(1), (1, 'get'))

if __name__ == '__main__':
    unittest.main()
