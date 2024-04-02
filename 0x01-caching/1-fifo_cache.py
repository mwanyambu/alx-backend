#!/usr/bin/env python3

""" FIFOCache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ class inherits from BaseCaching """


    def __init__(self):
        """ initializes FIFOCache """
        super().__init__()

    def put(self, key, item):
        """ add items to cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                key1 = next(iter(self.cache_data))
                print("DISCARD:", key1)
                del self.cache_data[key1]
            self.cache_data[key] = item

    def get(self, key):
        """ gets item by key from cache """
        if key is not None:
            return self.cache_data.get(key)
        return None
