"""
    Unit test cases for find anagram script.
"""

__author__ = 'me@kartheek.net (Karnati Kartheek)'

import unittest
from scripts import find_anagram

class LruCacheTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_lru_cache(self):
        words = ['gogole', 'legogo', 'Google', 'ggogle']
        self.assertEqual(
            find_anagram.get_anagrams('google', words), ['gogole', 'legogo'])
        
if __name__ == '__main__':
    unittest.main()