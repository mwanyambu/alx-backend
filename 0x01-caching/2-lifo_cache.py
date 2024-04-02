#!/usr/bin/env python3

""" LIFOCache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class inherits from BaseCaching """


    def __init__(self):
        """ initializes FIFOCache """
        super().__init__()

    def put(self, key, item):
        """ add items to cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                print("DISCARD:", last_key)
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """ gets item by key from cache """
        if key is not None:
            return self.cache_data.get(key)
        return None
