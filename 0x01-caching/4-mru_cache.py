#!/usr/bin/env python3

"""MRUCache """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ inherits from caching system BaseCaching """

    def __init__(self):
        """ initializes MRUCache """
        super().__init__()

    def put(self, key, item):
        """ adds items to cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            if len(self.cache_data) >= self.MAX_ITEMS:
                most_recent = list(self.cache_data.keys())[-1]
                print("DISCARD:", most_recent)
                del self.cache_data[most_recent]
            self.cache_data[key] = item

    def get(self, key):
        """ gets item by key """
        if key is not None:
            if key in self.cache_data:
                value = self.cache_data.pop(key)
                self.cache_data[key] = value
                return value
        return None
