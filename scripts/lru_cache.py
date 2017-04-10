"""
Simple python LRU cache management.

What is LRU Cache?
    An LRU cache is a Queue FIFO (First In First Out) data structure, which
    holds specific amount of data to enable quick lookup.

"""
__author__ = 'me@kartheek.net (Karnati Kartheek)'

from collections import OrderedDict, MutableMapping


class CacheData(MutableMapping):
    """To manipulate(set, get, remove, update) cached data. """

    def __init__(self, maxlen, *a, **k):
        self.maxlen = maxlen
        self.data = OrderedDict(*a, **k)
        while len(self) > maxlen:
            self.popitem()

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        val = self.data.pop(key)
        self.data[key] = val
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def __setitem__(self, key, val):
        if key not in self.data and len(self.data) == self.maxlen:
            self.popitem()
        self.data[key] = val


class lru_cache(object):
    """Creates cache object and manipulate the cache object based on the
       incoming value.
    """
    def __init__(self, maxsize=100):
        self.cache = CacheData(maxsize)

    def __call__(self, f):
        cache = self.cache

        def decorated(x):
            """Check requested value and update/create cache.
            Args:
                x: (int) value to check in cache
            Returns:
                (tuple) value, operation
            """
            val = cache.get(x)
            if val is None:
                val = f(x)
                cache[x] = val
                action = 'set'
            else:
                action = 'get'
            return (val, action)

        return decorated


@lru_cache(3)
def get_sqr(x):
    """To find square of given number.

    Args:
        x: value to get square.
    Returns:
        Square of the given value.
    """
    return x**2
